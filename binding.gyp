{
  "targets": [
    {
      "target_name": "kafka-native",
      "sources": [
        "src/kafka-native.cc",
        "src/common.cc",
        "src/producer.cc",
        "src/consumer.cc"
      ],
      'dependencies': [
        'librdkafka'
      ],
      "include_dirs": [
        "<!(node -e \"require('nan')\")",
        "deps/librdkafka/src"
      ],
      'conditions': [
        [
          'OS=="mac"',
          {
            'xcode_settings': {
              'MACOSX_DEPLOYMENT_TARGET': '10.11'
            },
            'libraries' : ['-lz']
          }
        ],[
          'OS=="linux" and gcc_version<=46',
          {
            'cflags': ['-std=c++0x','-g'],
            'libraries' : ['-lz']
          }
        ],[
          'OS=="linux" and gcc_version>46',
          {
            'cflags': ['-std=c++11','-g'],
            'libraries' : ['-lz', '-lssl', '-lsasl2']
          }
        ]
      ]
    },
    {
      "target_name": "librdkafka_config_h",
      "type": "none",
      "actions": [
        {
          'action_name': 'configure_librdkafka',
          'message': 'configuring librdkafka...',
          'inputs': [
            'deps/librdkafka/configure',
          ],
          'outputs': [
            'deps/librdkafka/config.h',
          ],
          'action': ['eval', 'cd deps/librdkafka && ./configure'],
        },
      ],
    },
    {
      "target_name": "librdkafka",
      "type": "static_library",
      'dependencies': [
        'librdkafka_config_h',
      ],
      "sources": [
        "deps/librdkafka/src/rdkafka_offset.c",
        "deps/librdkafka/src/rdkafka_op.c",
        "deps/librdkafka/src/rdkafka_partition.c",
        "deps/librdkafka/src/rdkafka_pattern.c",
        "deps/librdkafka/src/rdkafka_plugin.c",
        "deps/librdkafka/src/rdkafka_queue.c",
        "deps/librdkafka/src/rdkafka_range_assignor.c",
        "deps/librdkafka/src/rdkafka_request.c",
        "deps/librdkafka/src/rdkafka_roundrobin_assignor.c",
        "deps/librdkafka/src/rdkafka_sasl.c",
        "deps/librdkafka/src/rdkafka_sasl_cyrus.c",
        "deps/librdkafka/src/rdkafka_sasl_plain.c",
        "deps/librdkafka/src/rdkafka_sasl_scram.c",
        "deps/librdkafka/src/rdkafka_subscription.c",
        "deps/librdkafka/src/rdkafka_timer.c",
        "deps/librdkafka/src/rdkafka_topic.c",
        "deps/librdkafka/src/rdkafka_transport.c",
        "deps/librdkafka/src/rdlist.c",
        "deps/librdkafka/src/rdlog.c",
        "deps/librdkafka/src/rdports.c",
        "deps/librdkafka/src/rdrand.c",
        "deps/librdkafka/src/rdregex.c",
        "deps/librdkafka/src/rdstring.c",
        "deps/librdkafka/src/rdunittest.c",
        "deps/librdkafka/src/rdvarint.c",
        "deps/librdkafka/src/regexp.c",
        "deps/librdkafka/src/snappy.c",
        "deps/librdkafka/src/tinycthread.c",
        "deps/librdkafka/src/xxhash.c",
        "deps/librdkafka/src/crc32c.c",
        "deps/librdkafka/src/lz4.c",
        "deps/librdkafka/src/lz4frame.c",
        "deps/librdkafka/src/lz4hc.c",
        "deps/librdkafka/src/rdaddr.c",
        "deps/librdkafka/src/rdavl.c",
        "deps/librdkafka/src/rdbuf.c",
        "deps/librdkafka/src/rdcrc32.c",
        "deps/librdkafka/src/rddl.c",
        "deps/librdkafka/src/rdgz.c",
        "deps/librdkafka/src/rdkafka.c",
        "deps/librdkafka/src/rdkafka_assignor.c",
        "deps/librdkafka/src/rdkafka_broker.c",
        "deps/librdkafka/src/rdkafka_buf.c",
        "deps/librdkafka/src/rdkafka_cgrp.c",
        "deps/librdkafka/src/rdkafka_conf.c",
        "deps/librdkafka/src/rdkafka_event.c",
        "deps/librdkafka/src/rdkafka_feature.c",
        "deps/librdkafka/src/rdkafka_interceptor.c",
        "deps/librdkafka/src/rdkafka_lz4.c",
        "deps/librdkafka/src/rdkafka_metadata.c",
        "deps/librdkafka/src/rdkafka_metadata_cache.c",
        "deps/librdkafka/src/rdkafka_msg.c",
        "deps/librdkafka/src/rdkafka_msgset_reader.c",
        "deps/librdkafka/src/rdkafka_msgset_writer.c",
      ],
      'conditions': [
        [
          'OS=="mac"',
          {
            'xcode_settings': {
              'MACOSX_DEPLOYMENT_TARGET': '10.11',
              'OTHER_CFLAGS' : ['-Wno-sign-compare', '-Wno-missing-field-initializers'],
            },
            'libraries' : ['-lz']
          }
        ],[
          'OS=="linux"',
          {
            'cflags' : [ '-Wno-sign-compare', '-Wno-missing-field-initializers', '-Wno-empty-body', '-g'],
          }
        ]
      ]
    }
  ]
}
