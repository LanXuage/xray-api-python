# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proxy/dokodemo/config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common.net import address_pb2 as common_dot_net_dot_address__pb2
from common.net import network_pb2 as common_dot_net_dot_network__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bproxy/dokodemo/config.proto\x12\x13xray.proxy.dokodemo\x1a\x18\x63ommon/net/address.proto\x1a\x18\x63ommon/net/network.proto\"\xea\x01\n\x06\x43onfig\x12,\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32\x1b.xray.common.net.IPOrDomain\x12\x0c\n\x04port\x18\x02 \x01(\r\x12\x36\n\x0cnetwork_list\x18\x03 \x01(\x0b\x32\x1c.xray.common.net.NetworkListB\x02\x18\x01\x12*\n\x08networks\x18\x07 \x03(\x0e\x32\x18.xray.common.net.Network\x12\x13\n\x07timeout\x18\x04 \x01(\rB\x02\x18\x01\x12\x17\n\x0f\x66ollow_redirect\x18\x05 \x01(\x08\x12\x12\n\nuser_level\x18\x06 \x01(\rB[\n\x17\x63om.xray.proxy.dokodemoP\x01Z(github.com/xtls/xray-core/proxy/dokodemo\xaa\x02\x13Xray.Proxy.Dokodemob\x06proto3')



_CONFIG = DESCRIPTOR.message_types_by_name['Config']
Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), {
  'DESCRIPTOR' : _CONFIG,
  '__module__' : 'proxy.dokodemo.config_pb2'
  # @@protoc_insertion_point(class_scope:xray.proxy.dokodemo.Config)
  })
_sym_db.RegisterMessage(Config)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\027com.xray.proxy.dokodemoP\001Z(github.com/xtls/xray-core/proxy/dokodemo\252\002\023Xray.Proxy.Dokodemo'
  _CONFIG.fields_by_name['network_list']._options = None
  _CONFIG.fields_by_name['network_list']._serialized_options = b'\030\001'
  _CONFIG.fields_by_name['timeout']._options = None
  _CONFIG.fields_by_name['timeout']._serialized_options = b'\030\001'
  _CONFIG._serialized_start=105
  _CONFIG._serialized_end=339
# @@protoc_insertion_point(module_scope)
