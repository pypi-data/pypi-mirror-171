# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: RegisterResponse.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import AccessPointsConfig_pb2 as AccessPointsConfig__pb2
import SdkOption_pb2 as SdkOption__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16RegisterResponse.proto\x12\x13\x41\x63\x46unDanmu.Im.Basic\x1a\x18\x41\x63\x63\x65ssPointsConfig.proto\x1a\x0fSdkOption.proto\"\xef\x03\n\x10RegisterResponse\x12\x43\n\x12\x61\x63\x63\x65ssPointsConfig\x18\x01 \x01(\x0b\x32\'.AcFunDanmu.Im.Basic.AccessPointsConfig\x12\x0f\n\x07sessKey\x18\x02 \x01(\x0c\x12\x12\n\ninstanceId\x18\x03 \x01(\x03\x12\x31\n\tsdkOption\x18\x04 \x01(\x0b\x32\x1e.AcFunDanmu.Im.Basic.SdkOption\x12G\n\x16\x61\x63\x63\x65ssPointsConfigIpv6\x18\x05 \x01(\x0b\x32\'.AcFunDanmu.Im.Basic.AccessPointsConfig\x12G\n\x16\x61\x63\x63\x65ssPointsConfigQuic\x18\x06 \x01(\x0b\x32\'.AcFunDanmu.Im.Basic.AccessPointsConfig\x12K\n\x1a\x61\x63\x63\x65ssPointsConfigQuicIpv6\x18\x07 \x01(\x0b\x32\'.AcFunDanmu.Im.Basic.AccessPointsConfig\x12\x18\n\x10\x63leanAccessPoint\x18\x08 \x01(\x08\x12\x45\n\x14\x61\x63\x63\x65ssPointsConfigWs\x18\t \x01(\x0b\x32\'.AcFunDanmu.Im.Basic.AccessPointsConfigb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'RegisterResponse_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REGISTERRESPONSE._serialized_start=91
  _REGISTERRESPONSE._serialized_end=586
# @@protoc_insertion_point(module_scope)
