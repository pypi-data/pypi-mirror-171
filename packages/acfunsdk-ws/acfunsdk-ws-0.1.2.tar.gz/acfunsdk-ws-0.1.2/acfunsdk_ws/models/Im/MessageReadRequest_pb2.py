# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: MessageReadRequest.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ChatTargetType_pb2 as ChatTargetType__pb2
import User_pb2 as User__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18MessageReadRequest.proto\x12\x15\x41\x63\x46unDanmu.Im.Message\x1a\x14\x43hatTargetType.proto\x1a\nUser.proto\"\xb6\x01\n\x12MessageReadRequest\x12)\n\x06target\x18\x01 \x01(\x0b\x32\x19.AcFunDanmu.Im.Basic.User\x12\x0f\n\x07readSeq\x18\x02 \x01(\x03\x12\x10\n\x08targetId\x18\x03 \x01(\x03\x12\x13\n\x0bstrTargetId\x18\x04 \x01(\t\x12=\n\x0e\x63hatTargetType\x18\x05 \x01(\x0e\x32%.AcFunDanmu.Im.Message.ChatTargetTypeb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'MessageReadRequest_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MESSAGEREADREQUEST._serialized_start=86
  _MESSAGEREADREQUEST._serialized_end=268
# @@protoc_insertion_point(module_scope)
