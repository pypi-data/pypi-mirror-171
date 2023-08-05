/*
* Copyright 2022 Jetperch LLC
*
* Licensed under the Apache License, Version 2.0 (the "License");
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at
*
*     http://www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS,
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
* See the License for the specific language governing permissions and
* limitations under the License.
*/

#include "jsdrv.h"
#include "js110_api.h"
#include "jsdrv_prv/cdef.h"
#include "jsdrv_prv/log.h"
#include "jsdrv_prv/backend.h"
#include "jsdrv_prv/frontend.h"
#include "jsdrv_prv/js110_cal.h"
#include "jsdrv_prv/js110_sample_processor.h"
#include "jsdrv_prv/js110_stats.h"
#include "jsdrv_prv/msg_queue.h"
#include "jsdrv_prv/usb_spec.h"
#include "jsdrv_prv/thread.h"
#include "jsdrv_prv/pubsub.h"
#include "jsdrv/cstr.h"
#include "jsdrv/error_code.h"
#include "jsdrv/meta.h"
#include "jsdrv/topic.h"
#include "jsdrv_prv/dbc.h"
#include "jsdrv_prv/platform.h"
#include "tinyprintf.h"
#include <math.h>


#define TIMEOUT_MS  (1000U)
#define SENSOR_COMMAND_TIMEOUT_MS  (3000U)
#define FRAME_SIZE_BYTES           (512U)
#define ROE JSDRV_RETURN_ON_ERROR

struct js110_dev_s;  // forward declaration, see below

enum state_e {
    ST_NOT_PRESENT = 0,  //
    ST_CLOSED = 1,
    ST_OPENING = 2,
    ST_OPEN = 3,
};

static int32_t d_close(struct js110_dev_s * d);

typedef void (*param_fn)(struct js110_dev_s * d, const struct jsdrv_union_s * value);

struct param_s {
    const char * topic;
    const char * meta;
    param_fn fn;
};

static void on_i_range_select(struct js110_dev_s * d, const struct jsdrv_union_s * value);
static void on_v_range_select(struct js110_dev_s * d, const struct jsdrv_union_s * value);
static void on_extio_voltage(struct js110_dev_s * d, const struct jsdrv_union_s * value);
static void on_gpo0_value(struct js110_dev_s * d, const struct jsdrv_union_s * value);
static void on_gpo1_value(struct js110_dev_s * d, const struct jsdrv_union_s * value);
static void on_current_lsb_source(struct js110_dev_s * d, const struct jsdrv_union_s * value);
static void on_voltage_lsb_source(struct js110_dev_s * d, const struct jsdrv_union_s * value);

static void on_i_range_mode(struct js110_dev_s * d, const struct jsdrv_union_s * value);
static void on_i_range_pre(struct js110_dev_s * d, const struct jsdrv_union_s * value);
static void on_i_range_win(struct js110_dev_s * d, const struct jsdrv_union_s * value);
static void on_i_range_win_sz(struct js110_dev_s * d, const struct jsdrv_union_s * value);
static void on_i_range_post(struct js110_dev_s * d, const struct jsdrv_union_s * value);

static void on_current_ctrl(struct js110_dev_s * d, const struct jsdrv_union_s * value);
static void on_voltage_ctrl(struct js110_dev_s * d, const struct jsdrv_union_s * value);
static void on_power_ctrl(struct js110_dev_s * d, const struct jsdrv_union_s * value);
static void on_current_range_ctrl(struct js110_dev_s * d, const struct jsdrv_union_s * value);
static void on_gpi_0_ctrl(struct js110_dev_s * d, const struct jsdrv_union_s * value);
static void on_gpi_1_ctrl(struct js110_dev_s * d, const struct jsdrv_union_s * value);
static void on_stats_scnt(struct js110_dev_s * d, const struct jsdrv_union_s * value);
static void on_stats_ctrl(struct js110_dev_s * d, const struct jsdrv_union_s * value);

enum param_e {  // CAREFUL! This must match the order in PARAMS exactly!
    PARAM_I_RANGE_SELECT,
    PARAM_V_RANGE_SELECT,
    PARAM_EXTIO_VOLTAGE,
    PARAM_GPO0_VALUE,
    PARAM_GPO1_VALUE,
    PARAM_I_LSB_SOURCE,
    PARAM_V_LSB_SOURCE,
    PARAMS_I_RANGE_MODE,
    PARAMS_I_RANGE_PRE,
    PARAMS_I_RANGE_WIN,
    PARAMS_I_RANGE_WIN_SZ,
    PARAMS_I_RANGE_POST,
    PARAM_I_CTRL,
    PARAM_V_CTRL,
    PARAM_P_CTRL,
    PARAM_I_RANGE_CTRL,
    PARAM_GPI_0_CTRL,
    PARAM_GPI_1_CTRL,
    PARAM_STATS_SCNT,
    PARAM_STATS_CTRL,
    PARAM__COUNT,  // must be last
};


static const struct param_s PARAMS[] = {
    {
        "s/i/range/select",
        "{"
            "\"dtype\": \"u8\","
            "\"brief\": \"The current range selection.\","
            "\"default\": 0,"
            "\"options\": ["
                "[128, \"auto\"],"
                "[1, \"10 A\"],"
                "[2, \"2 A\"],"
                "[4, \"180 mA\"],"
                "[8, \"18 mA\"],"
                "[16, \"1.8 mA\"],"
                "[32, \"180 µA\"],"
                "[64, \"18 µA\"],"
                "[0, \"off\"]"
            "]"
        "}",
        on_i_range_select,
    },
    {
        "s/v/range/select",
        "{"
            "\"dtype\": \"u8\","
            "\"brief\": \"The voltage range selection.\","
            "\"default\": 0,"
            "\"options\": ["
                "[0, \"15 V\"],"
                "[1, \"5 V\"]"
            "]"
        "}",
        on_v_range_select,
    },
    {
        "s/extio/voltage",
        "{"
            "\"dtype\": \"u32\","
            "\"brief\": \"The external IO voltage.\","
            "\"default\": 3300,"
            "\"options\": ["
                "[0, \"0V\", \"off\"],"
                "[1800, \"1.8V\"],"
                "[2100, \"2.1V\"],"
                "[2500, \"2.5V\"],"
                "[2700, \"2.7V\"],"
                "[3000, \"3.0V\"],"
                "[3300, \"3.3V\"],"
                "[3600, \"3.6V\"],"
                "[5000, \"5.0V\"]"
            "]"
        "}",
        on_extio_voltage,
    },
    {
        "s/gpo/0/value",
        "{"
            "\"dtype\": \"bool\","
            "\"brief\": \"The general-purpose output 0 value.\","
            "\"default\": 0,"
            "\"options\": ["
                "[0, \"off\"],"
                "[1, \"on\"]"
            "]"
        "}",
        on_gpo0_value,
    },
    {
        "s/gpo/1/value",
        "{"
            "\"dtype\": \"bool\","
            "\"brief\": \"The general-purpose output 1 value.\","
            "\"default\": 0,"
            "\"options\": ["
                "[0, \"off\"],"
                "[1, \"on\"]"
            "]"
        "}",
        on_gpo1_value,
    },
    {
        "s/i/lsb_src",
        "{"
            "\"dtype\": \"u8\","
            "\"brief\": \"The current signal least-significant bit mapping.\","
            "\"default\": 0,"
            "\"options\": ["
                "[0, \"normal\"],"
                "[2, \"gpi0\"],"
                "[3, \"gpi1\"]"
            "]"
        "}",
        on_current_lsb_source,
    },
    {
        "s/v/lsb_src",
        "{"
            "\"dtype\": \"u8\","
            "\"brief\": \"The voltage signal least-significant bit mapping.\","
            "\"default\": 0,"
            "\"options\": ["
                "[0, \"normal\"],"
                "[2, \"gpi0\"],"
                "[3, \"gpi1\"]"
            "]"
        "}",
        on_voltage_lsb_source
    },
    {
        "s/i/range/mode",
        "{"
            "\"dtype\": \"u8\","
            "\"brief\": \"The current range suppression mode.\","
            "\"default\": 2,"
            "\"options\": ["
                "[0, \"off\"],"
                "[1, \"mean\"],"
                "[2, \"interp\", \"interpolate\"],"
                "[3, \"nan\"]"
            "]"
        "}",
        on_i_range_mode,
    },
    {
        "s/i/range/pre",
        "{"
            "\"dtype\": \"u8\","
            "\"brief\": \"The number of samples before the range switch to include.\","
            "\"default\": 1,"
            "\"range\": [0, 8]"
        "}",
        on_i_range_pre,
    },
    {
        "s/i/range/win",
        "{"
            "\"dtype\": \"u8\","
            "\"brief\": \"The window type.\","
            "\"default\": 2,"
            "\"options\": ["
                "[0, \"manual\"],"
                "[1, \"m\"],"
                "[2, \"n\"]"
            "]"
        "}",
        on_i_range_win,
    },
    {
        "s/i/range/win_sz",
        "{"
            "\"dtype\": \"u8\","
            "\"brief\": \"The manual window size.\","
            "\"default\": 10,"
            "\"range\": [0, 31]"
        "}",
        on_i_range_win_sz,
    },
    {
        "s/i/range/post",
        "{"
            "\"dtype\": \"u8\","
            "\"brief\": \"The number of samples after the range switch to include.\","
            "\"default\": 1,"
            "\"range\": [0, 8]"
        "}",
        on_i_range_post,
    },
    // buffer_duration
    // reduction_frequency
    // sampling_frequency (downsampling)
    // on-instrument statistics
    {
        "s/i/ctrl",
        "{"
            "\"dtype\": \"bool\","
            "\"brief\": \"Enable data stream for float32 current.\","
            "\"default\": 0"
        "}",
        on_current_ctrl,
    },
    {
        "s/v/ctrl",
        "{"
            "\"dtype\": \"bool\","
            "\"brief\": \"Enable data stream for float32 voltage.\","
            "\"default\": 0"
        "}",
        on_voltage_ctrl,
    },
    {
        "s/p/ctrl",
        "{"
            "\"dtype\": \"bool\","
            "\"brief\": \"Enable data stream for float32 power.\","
            "\"default\": 0"
        "}",
        on_power_ctrl,
    },
    {
        "s/i/range/ctrl",
        "{"
            "\"dtype\": \"bool\","
            "\"brief\": \"Enable current range input data stream (u4).\","
            "\"default\": 0"
        "}",
        on_current_range_ctrl,
    },
    {
        "s/gpi/0/ctrl",
        "{"
            "\"dtype\": \"bool\","
            "\"brief\": \"Enable general purpose input 0 data stream (u1).\","
            "\"default\": 0"
        "}",
        on_gpi_0_ctrl,
    },
    {
        "s/gpi/1/ctrl",
        "{"
            "\"dtype\": \"bool\","
            "\"brief\": \"Enable general purpose input 1 data stream (u1).\","
            "\"default\": 0"
        "}",
        on_gpi_1_ctrl,
    },
    {
        "s/stats/scnt",
        "{"
            "\"dtype\": \"u32\","
            "\"brief\": \"Number of 2 Msps samples per block.\","
            "\"default\": 1000000,"
            "\"range\": [0, 2000000]"
        "}",
        on_stats_scnt,
    },
    {
        "s/stats/ctrl",
        "{"
            "\"dtype\": \"bool\","
            "\"brief\": \"Enable stats input data stream (u8).\","
            "\"default\": 0"
        "}",
        on_stats_ctrl,
    },
    {NULL, NULL, NULL},  // MUST BE LAST
};


JSDRV_STATIC_ASSERT((PARAM__COUNT + 1) == JSDRV_ARRAY_SIZE(PARAMS), param_length_mismatch);


struct field_def_s {
    const char * data_topic;
    uint8_t field_id;                   // jsdrv_field_e
    uint8_t index;
    uint8_t element_type;               // jsdrv_data_type_e
    uint8_t element_size_bits;
    uint8_t downsample;
    enum param_e param;
};

#define FIELD(data_topic_, field_, index_, type_, size_, downsample_, param_) {    \
    .data_topic = (data_topic_),                                                        \
    .field_id=JSDRV_FIELD_##field_,                                                     \
    .index=(index_),                                                                    \
    .element_type=JSDRV_DATA_TYPE_##type_,                                              \
    .element_size_bits=(size_),                                                         \
    .downsample=(downsample_),                                                          \
    .param=(param_),                                                                    \
}

const struct field_def_s FIELDS[] = {
        //   (ctrl field,       data field, index, el_type, el_size_bits, downsample, param)
        FIELD("s/i/!data",       CURRENT,     0, FLOAT, 32, 1, PARAM_I_CTRL),
        FIELD("s/v/!data",       VOLTAGE,     0, FLOAT, 32, 1, PARAM_V_CTRL),
        FIELD("s/p/!data",       POWER,       0, FLOAT, 32, 1, PARAM_P_CTRL),
        FIELD("s/i/range/!data", RANGE,       0, UINT,   4, 1, PARAM_I_RANGE_CTRL),
        FIELD("s/gpi/0/!data",   GPI,         0, UINT,   1, 1, PARAM_GPI_0_CTRL),
        FIELD("s/gpi/1/!data",   GPI,         1, UINT,   1, 1, PARAM_GPI_1_CTRL),
};

struct port_s {
    uint64_t sample_id_next;
    struct jsdrvp_msg_s * msg;
};

struct js110_dev_s {
    struct jsdrvp_ul_device_s ul;
    struct jsdrvp_ll_device_s ll;
    struct jsdrv_context_s * context;
    uint8_t state; // state_e

    struct jsdrv_union_s param_values[JSDRV_ARRAY_SIZE(PARAMS)];
    uint64_t packet_index;
    struct js110_sp_s sample_processor;
    struct js110_stats_s stats;

    struct port_s ports[JSDRV_ARRAY_SIZE(FIELDS)];

    volatile bool do_exit;
    jsdrv_thread_t thread;
};

static bool handle_rsp(struct js110_dev_s * d, struct jsdrvp_msg_s * msg);

static const char * prefix_match_and_strip(const char * prefix, const char * topic) {
    while (*prefix) {
        if (*prefix++ != *topic++) {
            return NULL;
        }
    }
    if (*topic++ != '/') {
        return NULL;
    }
    return topic;
}

static struct jsdrvp_msg_s * ll_await_topic(struct js110_dev_s * d, const char * topic, uint32_t timeout_ms) {
    uint32_t t_now = jsdrv_time_ms_u32();
    uint32_t t_end = t_now + timeout_ms;

    while (1) {
#if _WIN32
        HANDLE h = msg_queue_handle_get(d->ll.rsp_q);
        WaitForSingleObject(h, timeout_ms);
#else
        struct pollfd fds = {
            .fd = msg_queue_handle_get(d->ll.rsp_q),
            .events = POLLIN,
            .revents = 0,
        };
        poll(&fds, 1, timeout_ms);
#endif
        struct jsdrvp_msg_s * m = msg_queue_pop_immediate(d->ll.rsp_q);
        if (!m) {
            // no message yet, keep trying until timeout.
        } else if (0 == strcmp(m->topic, topic)) {
            return m;
        } else {
            handle_rsp(d, m);
        }
        t_now = jsdrv_time_ms_u32();
        timeout_ms = t_end - t_now;
        if ((timeout_ms > (1U << 31U)) || (0 == timeout_ms)) {
            return NULL;
        }
    }
}

static void send_to_frontend(struct js110_dev_s * d, const char * subtopic, const struct jsdrv_union_s * value) {
    struct jsdrvp_msg_s * m;
    m = jsdrvp_msg_alloc_value(d->context, "", value);
    tfp_snprintf(m->topic, sizeof(m->topic), "%s/%s", d->ll.prefix, subtopic);
    jsdrvp_backend_send(d->context, m);
}

static int32_t jsdrvb_ctrl_out(struct js110_dev_s * d, usb_setup_t setup, const void * buffer) {
    struct jsdrvp_msg_s * m = jsdrvp_msg_alloc(d->context);
    jsdrv_cstr_copy(m->topic, JSDRV_USBBK_MSG_CTRL_IN, sizeof(m->topic));
    m->value.type = JSDRV_UNION_BIN;
    m->value.value.bin = m->payload.bin;
    m->value.app = JSDRV_PAYLOAD_TYPE_USB_CTRL;
    m->extra.bkusb_ctrl.setup = setup;
    if (setup.s.wLength > sizeof(m->payload.bin)) {
        JSDRV_LOGE("ctrl_out too big: %d", (int) setup.s.wLength);
        jsdrvp_msg_free(d->context, m);
        return JSDRV_ERROR_PARAMETER_INVALID;
    }
    memcpy(m->payload.bin, buffer, setup.s.wLength);
    m->value.size = setup.s.wLength;

    msg_queue_push(d->ll.cmd_q, m);
    m = ll_await_topic(d, JSDRV_USBBK_MSG_CTRL_IN, TIMEOUT_MS);
    if (!m) {
        JSDRV_LOGW("ctrl_out timed out");
        return JSDRV_ERROR_TIMED_OUT;
    }
    jsdrvp_msg_free(d->context, m);
    return 0;
}

static int32_t jsdrvb_ctrl_in(struct js110_dev_s * d, usb_setup_t setup, void * buffer, uint32_t * size) {
    int32_t rc = 0;
    struct jsdrvp_msg_s * m = jsdrvp_msg_alloc(d->context);
    jsdrv_cstr_copy(m->topic, JSDRV_USBBK_MSG_CTRL_OUT, sizeof(m->topic));
    m->value.type = JSDRV_UNION_BIN;
    m->value.value.bin = m->payload.bin;
    m->value.app = JSDRV_PAYLOAD_TYPE_USB_CTRL;
    m->extra.bkusb_ctrl.setup = setup;

    msg_queue_push(d->ll.cmd_q, m);
    m = ll_await_topic(d, JSDRV_USBBK_MSG_CTRL_OUT, TIMEOUT_MS);
    if (!m) {
        JSDRV_LOGW("ctrl_in timed out");
        return JSDRV_ERROR_TIMED_OUT;
    }
    if (m->value.size > setup.s.wLength) {
        JSDRV_LOGW("ctrl_in returned too much data");
        rc = JSDRV_ERROR_TOO_BIG;
    } else {
        memcpy(buffer, m->payload.bin, m->value.size);
        if (size) {
            *size = m->value.size;
        }
    }
    jsdrvp_msg_free(d->context, m);
    return rc;
}

static int32_t jsdrvb_bulk_in_stream_open(struct js110_dev_s * d, uint8_t endpoint) {
    struct jsdrvp_msg_s * m = jsdrvp_msg_alloc(d->context);
    jsdrv_cstr_copy(m->topic, JSDRV_USBBK_MSG_BULK_IN_STREAM_OPEN, sizeof(m->topic));
    m->value = jsdrv_union_i32(0);
    m->extra.bkusb_stream.endpoint = endpoint;
    msg_queue_push(d->ll.cmd_q, m);
    m = ll_await_topic(d, JSDRV_USBBK_MSG_BULK_IN_STREAM_OPEN, TIMEOUT_MS);
    if (!m) {
        JSDRV_LOGW("jsdrvb_bulk_in_stream_open timed out");
        return JSDRV_ERROR_TIMED_OUT;
    }
    int32_t rv = m->value.value.i32;;
    jsdrvp_msg_free(d->context, m);
    return rv;
}

static int32_t d_status(struct js110_dev_s * d, struct js110_host_status_s * status) {
    memset(status, 0, sizeof(*status));
    struct js110_host_packet_s pkt;
    usb_setup_t setup = { .s = {
            .bmRequestType = USB_REQUEST_TYPE(IN, VENDOR, DEVICE),
            .bRequest = JS110_HOST_USB_REQUEST_STATUS,
            .wValue = 0,
            .wIndex = 0,
            .wLength = 128,
    }};
    uint32_t sz = 0;
    int32_t rv = jsdrvb_ctrl_in(d, setup, &pkt, &sz);
    if (rv) {
        // do nothing
        JSDRV_LOGE("status returned %d", rv);
    } else if ((pkt.header.version == JS110_HOST_API_VERSION) && pkt.header.type == JS110_HOST_PACKET_TYPE_STATUS) {
        memcpy(status, &pkt.payload.status, sizeof(pkt.payload.status));
    } else {
        JSDRV_LOGW("unexpected message");
        rv = JSDRV_ERROR_UNSPECIFIED;  // unexpected
    }
    return rv;
}

static int32_t wait_for_sensor_command(struct js110_dev_s * d) {
    uint32_t t_start = jsdrv_time_ms_u32();
    while (1) {
        struct js110_host_status_s status;
        int32_t rv = d_status(d, &status);
        if (rv) {
            JSDRV_LOGW("status failed");
            return rv;
        }
        if ((status.settings_result == -1) || (status.settings_result == 19)) {
            // waiting, retry
        } else {
            JSDRV_LOGI("wait_for_sensor_command => %d", (int) rv);
            return rv;
        }
        if ((jsdrv_time_ms_u32() - t_start) > SENSOR_COMMAND_TIMEOUT_MS) {
            return JSDRV_ERROR_TIMED_OUT;
        }
    }
}

static bool is_streaming(struct js110_dev_s * d) {
    uint8_t stream_en =
            d->param_values[PARAM_I_CTRL].value.u8
            | d->param_values[PARAM_V_CTRL].value.u8
            | d->param_values[PARAM_P_CTRL].value.u8
            | d->param_values[PARAM_I_RANGE_CTRL].value.u8
            | d->param_values[PARAM_GPI_0_CTRL].value.u8
            | d->param_values[PARAM_GPI_1_CTRL].value.u8;
    return (0 != stream_en) ? true : false;
}

static int32_t calibration_get(struct js110_dev_s * d) {
    int32_t rv = 0;
    uint8_t * cal;
    uint8_t buf[4096];
    struct js110_cal_header_s hdr;
    usb_setup_t setup = { .s = {
            .bmRequestType = USB_REQUEST_TYPE(IN, VENDOR, DEVICE),
            .bRequest = JS110_HOST_USB_REQUEST_CALIBRATION,
            .wValue = 1,  // active calibration
            .wIndex = 0,
            .wLength = sizeof(hdr),
    }};
    uint32_t sz = 0;
    ROE(jsdrvb_ctrl_in(d, setup, &hdr, &sz));
    if (sz < sizeof(hdr)) {
        JSDRV_LOGW("cal too small");
        return JSDRV_ERROR_TOO_SMALL;
    }

    cal = jsdrv_alloc(hdr.length);
    uint32_t offset = 0;
    while (offset < hdr.length) {
        setup.s.wIndex = offset;
        uint32_t remaining = (uint32_t) (hdr.length - offset);
        setup.s.wLength = sizeof(buf);
        if (remaining < setup.s.wLength) {
            setup.s.wLength = remaining;
        }
        rv = jsdrvb_ctrl_in(d, setup, buf, &sz);
        if (rv) {
            break;
        }
        memcpy(cal + offset, buf, sz);
        offset += sz;
    }

    if (0 == rv) {
        rv = js110_cal_parse(cal, d->sample_processor.cal);
    }
    jsdrv_free(cal);
    return rv;
}

static int32_t stream_settings_send(struct js110_dev_s * d) {
    struct js110_host_packet_s pkt;
    memset(&pkt, 0, sizeof(pkt));
    // initialize device - configure for normal operation
    uint8_t v_range = d->param_values[PARAM_V_RANGE_SELECT].value.u8;
    uint8_t ovr_to_lsb = 0; // 0=off, 1=ovr to LSBs (not supported in this driver)
    pkt.header.version = JS110_HOST_API_VERSION;
    pkt.header.length = 16;
    pkt.header.type = JS110_HOST_PACKET_TYPE_SETTINGS;
    pkt.payload.settings.sensor_power = 1;
    pkt.payload.settings.select = d->param_values[PARAM_I_RANGE_SELECT].value.u8;
    pkt.payload.settings.source = 0xC0;     // raw ADC data
    pkt.payload.settings.options = ((v_range & 1) << 1) | (ovr_to_lsb & 1);
    pkt.payload.settings.streaming = is_streaming(d) ? 0x03 /* enable USB & FPGA */ : 0;

    usb_setup_t setup = { .s = {
            .bmRequestType = USB_REQUEST_TYPE(OUT, VENDOR, DEVICE),
            .bRequest = JS110_HOST_USB_REQUEST_SETTINGS,
            .wValue = 0,
            .wIndex = 0,
            .wLength = pkt.header.length,
    }};
    if (jsdrvb_ctrl_out(d, setup, &pkt)) {
        JSDRV_LOGW("stream_settings_send failed");
        return JSDRV_ERROR_IO;
    }
    if (wait_for_sensor_command(d)) {
        JSDRV_LOGW("stream_settings_send did not work");
        return JSDRV_ERROR_IO;
    }
    return 0;
}

static int32_t extio_settings_send(struct js110_dev_s * d) {
    struct js110_host_packet_s pkt;
    memset(&pkt, 0, sizeof(pkt));
    pkt.header.version = JS110_HOST_API_VERSION;
    pkt.header.length = 24;
    pkt.header.type = JS110_HOST_PACKET_TYPE_EXTIO;
    pkt.payload.extio.flags = 0;
    pkt.payload.extio.trigger_source = 0;
    pkt.payload.extio.current_gpi = d->param_values[PARAM_I_LSB_SOURCE].value.u8;
    pkt.payload.extio.voltage_gpi = d->param_values[PARAM_V_LSB_SOURCE].value.u8;
    pkt.payload.extio.gpo0 = d->param_values[PARAM_GPO0_VALUE].value.u8;
    pkt.payload.extio.gpo1 = d->param_values[PARAM_GPO1_VALUE].value.u8;
    pkt.payload.extio.io_voltage_mv = d->param_values[PARAM_EXTIO_VOLTAGE].value.u32;

    usb_setup_t setup = { .s = {
            .bmRequestType = USB_REQUEST_TYPE(OUT, VENDOR, DEVICE),
            .bRequest = JS110_HOST_USB_REQUEST_EXTIO,
            .wValue = 0,
            .wIndex = 0,
            .wLength = pkt.header.length,
    }};
    if (jsdrvb_ctrl_out(d, setup, &pkt)) {
        JSDRV_LOGW("extio_settings_send failed");
        return JSDRV_ERROR_IO;
    }
    if (wait_for_sensor_command(d)) {
        JSDRV_LOGW("extio_settings_send did not work");
        return JSDRV_ERROR_IO;
    }
    return 0;
}

static void on_i_range_select(struct js110_dev_s * d, const struct jsdrv_union_s * value) {
    d->param_values[PARAM_I_RANGE_SELECT] = *value;
    stream_settings_send(d);
}

static void on_v_range_select(struct js110_dev_s * d, const struct jsdrv_union_s * value) {
    d->param_values[PARAM_V_RANGE_SELECT] = *value;
    stream_settings_send(d);
}

static void on_extio_voltage(struct js110_dev_s * d, const struct jsdrv_union_s * value) {
    d->param_values[PARAM_EXTIO_VOLTAGE] = *value;
    extio_settings_send(d);
}

static void on_gpo0_value(struct js110_dev_s * d, const struct jsdrv_union_s * value) {
    d->param_values[PARAM_GPO0_VALUE] = *value;
    extio_settings_send(d);
}

static void on_gpo1_value(struct js110_dev_s * d, const struct jsdrv_union_s * value) {
    d->param_values[PARAM_GPO1_VALUE] = *value;
    extio_settings_send(d);
}

static void on_current_lsb_source(struct js110_dev_s * d, const struct jsdrv_union_s * value) {
    d->param_values[PARAM_I_LSB_SOURCE] = *value;
    extio_settings_send(d);
}

static void on_voltage_lsb_source(struct js110_dev_s * d, const struct jsdrv_union_s * value) {
    d->param_values[PARAM_V_LSB_SOURCE] = *value;
    extio_settings_send(d);
}

static void on_i_range_mode(struct js110_dev_s * d, const struct jsdrv_union_s * value) {
    d->sample_processor._suppress_mode = value->value.u8;
}

static void on_i_range_pre(struct js110_dev_s * d, const struct jsdrv_union_s * value) {
    d->sample_processor._suppress_samples_pre = value->value.u8;
}

static void on_i_range_win(struct js110_dev_s * d, const struct jsdrv_union_s * value) {
    js110_sp_suppress_win(&d->sample_processor, value->value.u8);
}

static void on_i_range_win_sz(struct js110_dev_s * d, const struct jsdrv_union_s * value) {
    d->sample_processor._suppress_samples_window = value->value.u8;
}

static void on_i_range_post(struct js110_dev_s * d, const struct jsdrv_union_s * value) {
    d->sample_processor._suppress_samples_post = value->value.u8;
}

static void on_update_ctrl(struct js110_dev_s * d, const struct jsdrv_union_s * value, int32_t param) {
    bool s1 = is_streaming(d);
    d->param_values[param] = *value;
    if (s1 != is_streaming(d)) {
        JSDRV_LOGI("on_update_ctrl %d (stream change)", param);
        if (!s1) {  // enabling streaming
            js110_sp_reset(&d->sample_processor);
            js110_stats_clear(&d->stats);
            d->packet_index = 0;
        } else {    // disabling streaming
            for (uint32_t idx = 0; idx < JSDRV_ARRAY_SIZE(FIELDS); ++idx) {
                struct port_s * p = &d->ports[idx];
                struct jsdrvp_msg_s *m = p->msg;
                p->msg = NULL;
                p->sample_id_next = 0;
                if (NULL != m) {
                    jsdrvp_msg_free(d->context, m);
                }
            }
        }
        stream_settings_send(d);
        JSDRV_LOGI("on_update_ctrl %d (stream change complete)", param);
    } else {
        JSDRV_LOGI("on_update_ctrl %d (no stream change)", param);
    }
}

static void on_current_ctrl(struct js110_dev_s * d, const struct jsdrv_union_s * value) {
    on_update_ctrl(d, value, PARAM_I_CTRL);
}

static void on_voltage_ctrl(struct js110_dev_s * d, const struct jsdrv_union_s * value) {
    on_update_ctrl(d, value, PARAM_V_CTRL);
}

static void on_power_ctrl(struct js110_dev_s * d, const struct jsdrv_union_s * value) {
    on_update_ctrl(d, value, PARAM_P_CTRL);
}

static void on_current_range_ctrl(struct js110_dev_s * d, const struct jsdrv_union_s * value) {
    on_update_ctrl(d, value, PARAM_I_RANGE_CTRL);
}

static void on_gpi_0_ctrl(struct js110_dev_s * d, const struct jsdrv_union_s * value) {
    on_update_ctrl(d, value, PARAM_GPI_0_CTRL);
}

static void on_gpi_1_ctrl(struct js110_dev_s * d, const struct jsdrv_union_s * value) {
    on_update_ctrl(d, value, PARAM_GPI_1_CTRL);
}

static void on_stats_scnt(struct js110_dev_s * d, const struct jsdrv_union_s * value) {
    struct jsdrv_union_s v = *value;
    jsdrv_union_as_type(&v, JSDRV_UNION_U32);
    js110_stats_sample_count_set(&d->stats, v.value.u32);
}

static void on_stats_ctrl(struct js110_dev_s * d, const struct jsdrv_union_s * value) {
    on_update_ctrl(d, value, PARAM_STATS_CTRL);
}

static int32_t d_open(struct js110_dev_s * d) {
    JSDRV_LOGI("open");
    struct jsdrvp_msg_s * m = jsdrvp_msg_alloc_value(d->context, JSDRV_MSG_OPEN, &jsdrv_union_i32(0));
    msg_queue_push(d->ll.cmd_q, m);
    m = ll_await_topic(d, JSDRV_MSG_OPEN, TIMEOUT_MS);
    if (!m) {
        JSDRV_LOGW("ll_driver open timed out");
        return JSDRV_ERROR_TIMED_OUT;
    }
    d->state = ST_OPENING;
    jsdrvp_msg_free(d->context, m);

    usb_setup_t setup = { .s = {
            .bmRequestType = USB_REQUEST_TYPE(OUT, VENDOR, DEVICE),
            .bRequest = JS110_HOST_USB_REQUEST_LOOPBACK_BUFFER,
            .wValue = 0,
            .wIndex = 0,
            .wLength = 16,
    }};
    uint8_t buf_out[16] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16};
    uint8_t buf_in[16];
    if (jsdrvb_ctrl_out(d, setup, buf_out)) {
        JSDRV_LOGW("ctrl loopback buffer write failed");
        return JSDRV_ERROR_IO;
    }
    setup.s.bmRequestType = USB_REQUEST_TYPE(IN, VENDOR, DEVICE);
    uint32_t sz;
    if (jsdrvb_ctrl_in(d, setup, buf_in, &sz)) {
        JSDRV_LOGW("ctrl loopback buffer read failed");
        return JSDRV_ERROR_IO;
    }

    if (0 != memcmp(buf_out, buf_in, sizeof(buf_in))) {
        JSDRV_LOGE("loopback failed");
    }

    ROE(stream_settings_send(d));
    ROE(calibration_get(d));

    // Publish topic metadata
    for (int i = 0; NULL != PARAMS[i].topic; ++i) {
        const struct param_s * p = &PARAMS[i];
        struct jsdrv_topic_s topic;
        jsdrv_topic_set(&topic, p->topic);
        jsdrv_topic_suffix_add(&topic, JSDRV_TOPIC_SUFFIX_METADATA_RSP);
        send_to_frontend(d, topic.topic, &jsdrv_union_cjson_r(p->meta));
    }

    // todo info_get(d) -> version, jsdrvb_ctrl_in JS110_HOST_USB_REQUEST_INFO

    // Publish topic values
    for (int i = 0; NULL != PARAMS[i].topic; ++i) {
        send_to_frontend(d, PARAMS[i].topic, &d->param_values[i]);
    }

    ROE(jsdrvb_bulk_in_stream_open(d, 2));

    JSDRV_LOGI("open complete");
    d->state = ST_OPEN;
    return 0;
}

static int32_t d_close(struct js110_dev_s * d) {
    JSDRV_LOGI("close");
    struct jsdrvp_msg_s * m = jsdrvp_msg_alloc_value(d->context, JSDRV_MSG_CLOSE, &jsdrv_union_u32(0));
    msg_queue_push(d->ll.cmd_q, m);
    m = ll_await_topic(d, JSDRV_MSG_CLOSE, TIMEOUT_MS);
    if (!m) {
        JSDRV_LOGW("ll_driver open timed out");
        return JSDRV_ERROR_TIMED_OUT;
    }
    d->state = ST_CLOSED;
    jsdrvp_msg_free(d->context, m);
    return 0;
}

static void handle_cmd_publish(struct js110_dev_s * d, const struct jsdrvp_msg_s * msg) {
    struct jsdrv_topic_s topic;
    const char * topic_str = prefix_match_and_strip(d->ll.prefix, msg->topic);
    jsdrv_topic_set(&topic, topic_str);
    jsdrv_topic_suffix_add(&topic, JSDRV_TOPIC_SUFFIX_RETURN_CODE);
    JSDRV_LOGI("handle_cmd_publish %s", topic_str);

    for (int i = 0; NULL != PARAMS[i].topic; ++i) {
        const struct param_s * p = &PARAMS[i];
        if (0 == strcmp(p->topic, topic_str)) {
            p->fn(d, &msg->value);
            send_to_frontend(d, topic.topic, &jsdrv_union_i32(0));
            return;
        }
    }
    JSDRV_LOGW("handle_cmd_publish %s not found", topic_str);
    send_to_frontend(d, topic.topic, &jsdrv_union_i32(JSDRV_ERROR_UNAVAILABLE));
}

static bool handle_cmd(struct js110_dev_s * d, struct jsdrvp_msg_s * msg) {
    int32_t status;
    bool rv = true;
    if (!msg) {
        return false;
    }
    const char * topic = prefix_match_and_strip(d->ll.prefix, msg->topic);
    if (msg->topic[0] == JSDRV_MSG_COMMAND_PREFIX_CHAR) {
        if (0 == strcmp(JSDRV_MSG_FINALIZE, msg->topic)) {
            // full driver shutdown
            d->do_exit = true;
            rv = false;
        } else {
            JSDRV_LOGE("handle_cmd unsupported %s", msg->topic);
        }
    } else if (!topic) {
        JSDRV_LOGE("handle_cmd mismatch %s, %s", msg->topic, d->ll.prefix);
    } else if (topic[0] == JSDRV_MSG_COMMAND_PREFIX_CHAR) {
        if (0 == strcmp(JSDRV_MSG_OPEN, topic)) {
            status = d_open(d);
            send_to_frontend(d, JSDRV_MSG_OPEN "#", &jsdrv_union_i32(status));
            if (status) {
                d_close(d);
            }
        } else if (0 == strcmp(JSDRV_MSG_CLOSE, topic)) {
            status = d_close(d);
            send_to_frontend(d, JSDRV_MSG_CLOSE "#", &jsdrv_union_i32(status));
        } else if (0 == strcmp(JSDRV_MSG_FINALIZE, msg->topic)) {
            // just finalize this upper-level driver (keep lower-level running)
            d->do_exit = true;
            rv = false;
        } else {
            JSDRV_LOGE("handle_cmd unsupported %s", msg->topic);
        }
    } else if (d->state != ST_OPEN) {
        send_to_frontend(d, topic, &jsdrv_union_i32(JSDRV_ERROR_CLOSED));
    } else {
        handle_cmd_publish(d, msg);
    }
    jsdrvp_msg_free(d->context, msg);
    return rv;
}

static struct jsdrvp_msg_s * field_message_get(struct js110_dev_s * d, uint8_t field_idx) {
    struct jsdrv_stream_signal_s * s;
    const struct field_def_s * field_def = &FIELDS[field_idx];
    struct jsdrvp_msg_s * m;
    struct port_s * p = &d->ports[field_idx];

    if (0 == d->param_values[field_def->param].value.u8) {
        if (p->msg) {
            JSDRV_LOGI("channel disabled, discard partial message");
            jsdrvp_msg_free(d->context, p->msg);
            p->msg = NULL;
        }
        return NULL;
    }

    if (NULL == p->msg) {
        m = jsdrvp_msg_alloc_data(d->context, "");
        tfp_snprintf(m->topic, sizeof(m->topic), "%s/%s", d->ll.prefix, field_def->data_topic);
        s = (struct jsdrv_stream_signal_s *) m->value.value.bin;
        s->sample_id = p->sample_id_next;
        s->index = field_def->index;
        s->field_id = field_def->field_id;
        s->element_type = field_def->element_type;
        s->element_size_bits = field_def->element_size_bits;
        s->element_count = 0;
        m->u32_a = (uint32_t) p->sample_id_next;
        m->value.app = JSDRV_PAYLOAD_TYPE_STREAM;
        m->value.size = JSDRV_STREAM_HEADER_SIZE;
        p->msg = m;
    }

    return p->msg;
}

static void field_message_process_end(struct js110_dev_s * d, uint8_t idx) {
    struct port_s * p = &d->ports[idx];
    struct jsdrvp_msg_s * m = p->msg;
    struct jsdrv_stream_signal_s * s = (struct jsdrv_stream_signal_s *) m->value.value.bin;
    ++s->element_count;
    ++p->sample_id_next;
    if ((s->element_size_bits < 8) && (((s->element_count * s->element_size_bits) & 0x7) != 0)) {
        return;
    }
    if ((((s->element_count * s->element_size_bits) / 8) >= JSDRV_STREAM_DATA_SIZE)
            || (s->element_count >= (2000000 / 20))) {  // todo support downsampling
        jsdrvp_backend_send(d->context, p->msg);
        p->msg = NULL;
    }
}

static void add_f32_field(struct js110_dev_s * d, uint8_t field_idx, float value) {
    struct jsdrvp_msg_s * m = field_message_get(d, field_idx);
    if (NULL == m) {
        return;
    }
    struct jsdrv_stream_signal_s * s = (struct jsdrv_stream_signal_s *) m->value.value.bin;
    float *data = (float *) s->data;
    data[s->element_count] = value;
    field_message_process_end(d, field_idx);
}

static void add_u4_field(struct js110_dev_s * d, uint8_t field_idx, uint8_t value) {
    struct jsdrv_stream_signal_s * s;
    struct jsdrvp_msg_s * m = field_message_get(d, field_idx);
    if (NULL == m) {
        return;
    }
    s = (struct jsdrv_stream_signal_s *) m->value.value.bin;
    value = value & 0x0f;
    if (0 == (s->element_count & 1)) {
        s->data[s->element_count >> 1] = value;
    } else {
        s->data[s->element_count >> 1] |= (value << 4);
    }
    field_message_process_end(d, field_idx);
}

static void add_u1_field(struct js110_dev_s * d, uint8_t field_idx, uint8_t value) {
    struct jsdrv_stream_signal_s * s;
    struct jsdrvp_msg_s * m = field_message_get(d, field_idx);
    if (NULL == m) {
        return;
    }
    s = (struct jsdrv_stream_signal_s *) m->value.value.bin;
    value = value & 1;
    if (0 == (s->element_count & 7)) {
        s->data[s->element_count >> 3] = value;
    } else {
        s->data[s->element_count >> 3] |= value << (s->element_count & 7);
    }
    field_message_process_end(d, field_idx);
}

static void handle_sample(struct js110_dev_s * d, uint32_t sample, uint8_t v_range) {
    struct js110_sample_s z = js110_sp_process(&d->sample_processor, sample, v_range);
    add_f32_field(d, 0, z.i);
    add_f32_field(d, 1, z.v);
    add_f32_field(d, 2, z.p);
    add_u4_field(d, 3, z.current_range);
    add_u1_field(d, 4, z.gpi0);
    add_u1_field(d, 5, z.gpi1);

    struct jsdrv_statistics_s * s = js110_stats_compute(&d->stats, z.i, z.v, z.p);
    if (NULL != s) {
        struct jsdrvp_msg_s * m = jsdrvp_msg_alloc(d->context);
        tfp_snprintf(m->topic, sizeof(m->topic), "%s/s/stats/value", d->ll.prefix);
        struct jsdrv_statistics_s * dst = (struct jsdrv_statistics_s *) m->payload.bin;
        *dst = *s;
        m->value = jsdrv_union_cbin_r((uint8_t *) dst, sizeof(*dst));
        m->value.app = JSDRV_PAYLOAD_TYPE_STATISTICS;
        jsdrvp_backend_send(d->context, m);
    }
}

static void handle_stream_in_frame(struct js110_dev_s * d, uint32_t * p_u32) {
    uint8_t * p_u8 = (uint8_t *) p_u32;
    uint8_t buffer_type = p_u8[0];
    if (1 != buffer_type) {
        JSDRV_LOGW("handle_stream_in_frame invalid buffer type: %d", (int) buffer_type);
        return;
    }
    uint8_t status = p_u8[1];
    uint16_t pkt_length = ((uint16_t) p_u8[2]) | (((uint16_t) (p_u8[3] & 0x7f)) << 8);
    uint8_t voltage_range = (p_u8[3] >> 7) & 1;
    uint64_t pkt_index = ((uint16_t) p_u8[4]) | (((uint16_t) p_u8[5]) << 8);
    if (status) {
        JSDRV_LOGW("handle_stream_in_frame status = %d", (int) status);
        return;
    }
    if (FRAME_SIZE_BYTES != pkt_length) {
        JSDRV_LOGW("handle_stream_in_frame invalid length = %d", (int) pkt_length);
        return;
    }
    if ((d->packet_index & 0xffff) != pkt_index) {
        JSDRV_LOGW("pkt_index skip: expected %d, received %d", d->packet_index, pkt_index);
        //while ((d->packet_index & 0xffff) != pkt_index) {
        //    for (uint32_t i = 2; i < (FRAME_SIZE_BYTES / 4); ++i) {
        //        handle_sample(d, 0xffffffffLU, voltage_range);
        //    }
        //    d->packet_index = (d->packet_index + 1) & 0xffff;
        //}
        // todo handle skips better.
        d->packet_index = pkt_index;
    }
    for (uint32_t i = 2; i < (FRAME_SIZE_BYTES / 4); ++i) {
        handle_sample(d, p_u32[i], voltage_range);
    }
    d->packet_index = (d->packet_index + 1) & 0xffff;
}

static void handle_stream_in(struct js110_dev_s * d, struct jsdrvp_msg_s * msg) {
    JSDRV_ASSERT(msg->value.type == JSDRV_UNION_BIN);
    uint32_t frame_count = (msg->value.size + FRAME_SIZE_BYTES - 1) / FRAME_SIZE_BYTES;
    for (uint32_t i = 0; i < frame_count; ++i) {
        uint32_t * p_u32 = (uint32_t *) &msg->value.value.bin[i * FRAME_SIZE_BYTES];
        handle_stream_in_frame(d, p_u32);
    }
}

static bool handle_rsp(struct js110_dev_s * d, struct jsdrvp_msg_s * msg) {
    bool rv = true;
    if (!msg) {
        return false;
    }
    if (0 == strcmp(JSDRV_USBBK_MSG_STREAM_IN_DATA, msg->topic)) {
        handle_stream_in(d, msg);
        msg_queue_push(d->ll.cmd_q, msg);  // return
        return true;
    } else if (msg->topic[0] == JSDRV_MSG_COMMAND_PREFIX_CHAR) {
        if (0 == strcmp(JSDRV_MSG_FINALIZE, msg->topic)) {
            d->do_exit = true;
            rv = false;
        } else {
            JSDRV_LOGE("handle_rsp unsupported command %s", msg->topic);
        }
    } else {
        JSDRV_LOGE("handle_rsp unsupported %s", msg->topic);
    }
    jsdrvp_msg_free(d->context, msg);
    return rv;
}

static THREAD_RETURN_TYPE driver_thread(THREAD_ARG_TYPE lpParam) {
    struct js110_dev_s *d = (struct js110_dev_s *) lpParam;
    JSDRV_LOGI("JS110 USB upper-level thread started %s", d->ll.prefix);

#if _WIN32
    HANDLE handles[MAXIMUM_WAIT_OBJECTS];
    DWORD handle_count = 0;
    handles[0] = msg_queue_handle_get(d->ul.cmd_q);
    handles[1] = msg_queue_handle_get(d->ll.rsp_q);
    handle_count = 2;
#else
    struct pollfd fds[2];
    fds[0].fd = msg_queue_handle_get(d->ul.cmd_q);
    fds[0].events = POLLIN;
    fds[1].fd = msg_queue_handle_get(d->ul.cmd_q);
    fds[1].events = POLLIN;
#endif

    while (!d->do_exit) {
#if _WIN32
        WaitForMultipleObjects(handle_count, handles, false, 5000);
#else
        poll(fds, 2, 5000);
#endif
        //JSDRV_LOGD3("ul thread");
        while (handle_cmd(d, msg_queue_pop_immediate(d->ul.cmd_q))) {
            ;
        }
        // note: ResetEvent handled automatically by msg_queue_pop_immediate
        while (handle_rsp(d, msg_queue_pop_immediate(d->ll.rsp_q))) {
            ;
        }
    }

    JSDRV_LOGI("JS110 USB upper-level thread done %s", d->ll.prefix);
    THREAD_RETURN();
}

static void join(struct jsdrvp_ul_device_s * device) {
    struct js110_dev_s * d = (struct js110_dev_s *) device;
    jsdrvp_send_finalize_msg(d->context, d->ul.cmd_q, "");
    // and wait for thread to exit.
    jsdrv_thread_join(&d->thread, 1000);
    jsdrv_free(d);
}

int32_t jsdrvp_ul_js110_usb_factory(struct jsdrvp_ul_device_s ** device, struct jsdrv_context_s * context, struct jsdrvp_ll_device_s * ll) {
    JSDRV_DBC_NOT_NULL(device);
    JSDRV_DBC_NOT_NULL(context);
    JSDRV_DBC_NOT_NULL(ll);
    *device = NULL;
    struct js110_dev_s * d = jsdrv_alloc_clr(sizeof(struct js110_dev_s));
    d->context = context;
    d->ll = *ll;
    d->ul.cmd_q = msg_queue_init();
    d->ul.join = join;
    d->state = ST_CLOSED;
    js110_sp_initialize(&d->sample_processor);

    for (int i = 0; NULL != PARAMS[i].topic; ++i) {
        jsdrv_meta_default(PARAMS[i].meta, &d->param_values[i]);
    }

    if (jsdrv_thread_create(&d->thread, driver_thread, d)) {
        return JSDRV_ERROR_UNSPECIFIED;
    }
#if _WIN32
    if (!SetThreadPriority(d->thread.thread, THREAD_PRIORITY_ABOVE_NORMAL)) {
        WINDOWS_LOGE("%s", "SetThreadPriority");
    }
#endif
    *device = &d->ul;
    return 0;
}
