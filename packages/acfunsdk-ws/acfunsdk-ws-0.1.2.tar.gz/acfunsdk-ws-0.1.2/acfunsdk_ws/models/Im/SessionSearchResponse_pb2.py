# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: SessionSearchResponse.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import GroupMsgSearchResult_pb2 as GroupMsgSearchResult__pb2
import UserMsgSearchResult_pb2 as UserMsgSearchResult__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bSessionSearchResponse.proto\x12\x1a\x41\x63\x46unDanmu.Im.Cloud.Search\x1a\x1aGroupMsgSearchResult.proto\x1a\x19UserMsgSearchResult.proto\"\xa3\x01\n\x15SessionSearchResponse\x12\x43\n\nuserResult\x18\x01 \x03(\x0b\x32/.AcFunDanmu.Im.Cloud.Search.UserMsgSearchResult\x12\x45\n\x0bgroupResult\x18\x02 \x03(\x0b\x32\x30.AcFunDanmu.Im.Cloud.Search.GroupMsgSearchResultb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'SessionSearchResponse_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SESSIONSEARCHRESPONSE._serialized_start=115
  _SESSIONSEARCHRESPONSE._serialized_end=278
# @@protoc_insertion_point(module_scope)
