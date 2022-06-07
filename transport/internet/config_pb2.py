# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: transport/internet/config.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common.serial import typed_message_pb2 as common_dot_serial_dot_typed__message__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ftransport/internet/config.proto\x12\x17xray.transport.internet\x1a!common/serial/typed_message.proto\"\x9e\x01\n\x0fTransportConfig\x12@\n\x08protocol\x18\x01 \x01(\x0e\x32*.xray.transport.internet.TransportProtocolB\x02\x18\x01\x12\x15\n\rprotocol_name\x18\x03 \x01(\t\x12\x32\n\x08settings\x18\x02 \x01(\x0b\x32 .xray.common.serial.TypedMessage\"\xc1\x02\n\x0cStreamConfig\x12@\n\x08protocol\x18\x01 \x01(\x0e\x32*.xray.transport.internet.TransportProtocolB\x02\x18\x01\x12\x15\n\rprotocol_name\x18\x05 \x01(\t\x12\x44\n\x12transport_settings\x18\x02 \x03(\x0b\x32(.xray.transport.internet.TransportConfig\x12\x15\n\rsecurity_type\x18\x03 \x01(\t\x12;\n\x11security_settings\x18\x04 \x03(\x0b\x32 .xray.common.serial.TypedMessage\x12>\n\x0fsocket_settings\x18\x06 \x01(\x0b\x32%.xray.transport.internet.SocketConfig\"7\n\x0bProxyConfig\x12\x0b\n\x03tag\x18\x01 \x01(\t\x12\x1b\n\x13transportLayerProxy\x18\x02 \x01(\x08\"\x84\x03\n\x0cSocketConfig\x12\x0c\n\x04mark\x18\x01 \x01(\x05\x12\x0b\n\x03tfo\x18\x02 \x01(\x05\x12@\n\x06tproxy\x18\x03 \x01(\x0e\x32\x30.xray.transport.internet.SocketConfig.TProxyMode\x12%\n\x1dreceive_original_dest_address\x18\x04 \x01(\x08\x12\x14\n\x0c\x62ind_address\x18\x05 \x01(\x0c\x12\x11\n\tbind_port\x18\x06 \x01(\r\x12\x1d\n\x15\x61\x63\x63\x65pt_proxy_protocol\x18\x07 \x01(\x08\x12@\n\x0f\x64omain_strategy\x18\x08 \x01(\x0e\x32\'.xray.transport.internet.DomainStrategy\x12\x14\n\x0c\x64ialer_proxy\x18\t \x01(\t\x12\x1f\n\x17tcp_keep_alive_interval\x18\n \x01(\x05\"/\n\nTProxyMode\x12\x07\n\x03Off\x10\x00\x12\n\n\x06TProxy\x10\x01\x12\x0c\n\x08Redirect\x10\x02*Z\n\x11TransportProtocol\x12\x07\n\x03TCP\x10\x00\x12\x07\n\x03UDP\x10\x01\x12\x08\n\x04MKCP\x10\x02\x12\r\n\tWebSocket\x10\x03\x12\x08\n\x04HTTP\x10\x04\x12\x10\n\x0c\x44omainSocket\x10\x05*A\n\x0e\x44omainStrategy\x12\t\n\x05\x41S_IS\x10\x00\x12\n\n\x06USE_IP\x10\x01\x12\x0b\n\x07USE_IP4\x10\x02\x12\x0b\n\x07USE_IP6\x10\x03\x42g\n\x1b\x63om.xray.transport.internetP\x01Z,github.com/xtls/xray-core/transport/internet\xaa\x02\x17Xray.Transport.Internetb\x06proto3')

_TRANSPORTPROTOCOL = DESCRIPTOR.enum_types_by_name['TransportProtocol']
TransportProtocol = enum_type_wrapper.EnumTypeWrapper(_TRANSPORTPROTOCOL)
_DOMAINSTRATEGY = DESCRIPTOR.enum_types_by_name['DomainStrategy']
DomainStrategy = enum_type_wrapper.EnumTypeWrapper(_DOMAINSTRATEGY)
TCP = 0
UDP = 1
MKCP = 2
WebSocket = 3
HTTP = 4
DomainSocket = 5
AS_IS = 0
USE_IP = 1
USE_IP4 = 2
USE_IP6 = 3


_TRANSPORTCONFIG = DESCRIPTOR.message_types_by_name['TransportConfig']
_STREAMCONFIG = DESCRIPTOR.message_types_by_name['StreamConfig']
_PROXYCONFIG = DESCRIPTOR.message_types_by_name['ProxyConfig']
_SOCKETCONFIG = DESCRIPTOR.message_types_by_name['SocketConfig']
_SOCKETCONFIG_TPROXYMODE = _SOCKETCONFIG.enum_types_by_name['TProxyMode']
TransportConfig = _reflection.GeneratedProtocolMessageType('TransportConfig', (_message.Message,), {
  'DESCRIPTOR' : _TRANSPORTCONFIG,
  '__module__' : 'transport.internet.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.transport.internet.TransportConfig)
  })
_sym_db.RegisterMessage(TransportConfig)

StreamConfig = _reflection.GeneratedProtocolMessageType('StreamConfig', (_message.Message,), {
  'DESCRIPTOR' : _STREAMCONFIG,
  '__module__' : 'transport.internet.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.transport.internet.StreamConfig)
  })
_sym_db.RegisterMessage(StreamConfig)

ProxyConfig = _reflection.GeneratedProtocolMessageType('ProxyConfig', (_message.Message,), {
  'DESCRIPTOR' : _PROXYCONFIG,
  '__module__' : 'transport.internet.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.transport.internet.ProxyConfig)
  })
_sym_db.RegisterMessage(ProxyConfig)

SocketConfig = _reflection.GeneratedProtocolMessageType('SocketConfig', (_message.Message,), {
  'DESCRIPTOR' : _SOCKETCONFIG,
  '__module__' : 'transport.internet.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.transport.internet.SocketConfig)
  })
_sym_db.RegisterMessage(SocketConfig)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\033com.xray.transport.internetP\001Z,github.com/xtls/xray-core/transport/internet\252\002\027Xray.Transport.Internet'
  _TRANSPORTCONFIG.fields_by_name['protocol']._options = None
  _TRANSPORTCONFIG.fields_by_name['protocol']._serialized_options = b'\030\001'
  _STREAMCONFIG.fields_by_name['protocol']._options = None
  _STREAMCONFIG.fields_by_name['protocol']._serialized_options = b'\030\001'
  _TRANSPORTPROTOCOL._serialized_start=1028
  _TRANSPORTPROTOCOL._serialized_end=1118
  _DOMAINSTRATEGY._serialized_start=1120
  _DOMAINSTRATEGY._serialized_end=1185
  _TRANSPORTCONFIG._serialized_start=96
  _TRANSPORTCONFIG._serialized_end=254
  _STREAMCONFIG._serialized_start=257
  _STREAMCONFIG._serialized_end=578
  _PROXYCONFIG._serialized_start=580
  _PROXYCONFIG._serialized_end=635
  _SOCKETCONFIG._serialized_start=638
  _SOCKETCONFIG._serialized_end=1026
  _SOCKETCONFIG_TPROXYMODE._serialized_start=979
  _SOCKETCONFIG_TPROXYMODE._serialized_end=1026
# @@protoc_insertion_point(module_scope)