#!/bin/env pythn3
#-*- author: xuage -*-
import grpc
from core import config_pb2 as core_config_pb2

from app.proxyman.command import command_pb2, command_pb2_grpc
from app.proxyman import config_pb2 as app_proxyman_config_pb2
from proxy.vmess.inbound import config_pb2 as proxy_vmess_inbound_config_pb2
from common.net import address_pb2, port_pb2
from common.serial import typed_message_pb2


if __name__ == '__main__':
    with grpc.insecure_channel('localhost:10085') as channel:
        stub = command_pb2_grpc.HandlerServiceStub(channel)
        range_i = port_pb2.PortRange(From=8080, To=8081)
        port_list = port_pb2.PortList()
        port_list.range.append(range_i)
        listen = address_pb2.IPOrDomain(ip=b'\x7f\x00\x00\x01')
        receiver_settings = app_proxyman_config_pb2.ReceiverConfig(port_list=port_list, listen=listen)
        print(type(receiver_settings))
        proxy_settings = proxy_vmess_inbound_config_pb2.Config()
        print(type(proxy_settings))
        ihc = core_config_pb2.InboundHandlerConfig(tag='grpctest', receiver_settings=typed_message_pb2.TypedMessage(type=receiver_settings.DESCRIPTOR.full_name, value=receiver_settings.SerializeToString()), proxy_settings=typed_message_pb2.TypedMessage(type=proxy_settings.DESCRIPTOR.full_name, value=proxy_settings.SerializeToString()))
        print(ihc)
        air = command_pb2.AddInboundRequest(inbound=ihc)
        print(air)
        resp = stub.AddInbound(air)
        print(resp)
        
