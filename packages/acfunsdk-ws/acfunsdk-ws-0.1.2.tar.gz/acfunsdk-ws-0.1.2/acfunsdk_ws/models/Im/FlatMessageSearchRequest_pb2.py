# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: FlatMessageSearchRequest.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ImcMessageType_pb2 as ImcMessageType__pb2
import TimeFilter_pb2 as TimeFilter__pb2
import User_pb2 as User__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1e\x46latMessageSearchRequest.proto\x12\x1a\x41\x63\x46unDanmu.Im.Cloud.Search\x1a\x14ImcMessageType.proto\x1a\x10TimeFilter.proto\x1a\nUser.proto\"\x94\x02\n\x18\x46latMessageSearchRequest\x12\r\n\x05query\x18\x01 \x03(\t\x12\'\n\x04\x66rom\x18\x02 \x03(\x0b\x32\x19.AcFunDanmu.Im.Basic.User\x12<\n\x07msgType\x18\x03 \x01(\x0e\x32+.AcFunDanmu.Im.Cloud.Message.ImcMessageType\x12\x0f\n\x07groupId\x18\x04 \x03(\t\x12:\n\ntimeFilter\x18\x05 \x01(\x0b\x32&.AcFunDanmu.Im.Cloud.Search.TimeFilter\x12\x0e\n\x06offset\x18\x06 \x01(\t\x12\x10\n\x08msgCount\x18\x07 \x01(\x05\x12\x13\n\x0bmessageType\x18\x08 \x03(\x05\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'FlatMessageSearchRequest_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _FLATMESSAGESEARCHREQUEST._serialized_start=115
  _FLATMESSAGESEARCHREQUEST._serialized_end=391
# @@protoc_insertion_point(module_scope)
