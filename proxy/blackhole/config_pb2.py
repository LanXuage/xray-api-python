# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proxy/blackhole/config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common.serial import typed_message_pb2 as common_dot_serial_dot_typed__message__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cproxy/blackhole/config.proto\x12\x14xray.proxy.blackhole\x1a!common/serial/typed_message.proto\"\x0e\n\x0cNoneResponse\"\x0e\n\x0cHTTPResponse\"<\n\x06\x43onfig\x12\x32\n\x08response\x18\x01 \x01(\x0b\x32 .xray.common.serial.TypedMessageB^\n\x18\x63om.xray.proxy.blackholeP\x01Z)github.com/xtls/xray-core/proxy/blackhole\xaa\x02\x14Xray.Proxy.Blackholeb\x06proto3')



_NONERESPONSE = DESCRIPTOR.message_types_by_name['NoneResponse']
_HTTPRESPONSE = DESCRIPTOR.message_types_by_name['HTTPResponse']
_CONFIG = DESCRIPTOR.message_types_by_name['Config']
NoneResponse = _reflection.GeneratedProtocolMessageType('NoneResponse', (_message.Message,), {
  'DESCRIPTOR' : _NONERESPONSE,
  '__module__' : 'proxy.blackhole.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.proxy.blackhole.NoneResponse)
  })
_sym_db.RegisterMessage(NoneResponse)

HTTPResponse = _reflection.GeneratedProtocolMessageType('HTTPResponse', (_message.Message,), {
  'DESCRIPTOR' : _HTTPRESPONSE,
  '__module__' : 'proxy.blackhole.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.proxy.blackhole.HTTPResponse)
  })
_sym_db.RegisterMessage(HTTPResponse)

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'proxy.blackhole.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.proxy.blackhole.Config)
  })
_sym_db.RegisterMessage(Config)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\030com.xray.proxy.blackholeP\001Z)github.com/xtls/xray-core/proxy/blackhole\252\002\024Xray.Proxy.Blackhole'
  _NONERESPONSE._serialized_start=89
  _NONERESPONSE._serialized_end=103
  _HTTPRESPONSE._serialized_start=105
  _HTTPRESPONSE._serialized_end=119
  _CONFIG._serialized_start=121
  _CONFIG._serialized_end=181
# @@protoc_insertion_point(module_scope)
