# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GroupCreateRequest.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import GroupLabel_pb2 as GroupLabel__pb2
import GroupType_pb2 as GroupType__pb2
import Location_pb2 as Location__pb2
import User_pb2 as User__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18GroupCreateRequest.proto\x12\x1b\x41\x63\x46unDanmu.Im.Cloud.Message\x1a\x10GroupLabel.proto\x1a\x0fGroupType.proto\x1a\x0eLocation.proto\x1a\nUser.proto\"\xd0\x02\n\x12GroupCreateRequest\x12*\n\x07members\x18\x01 \x03(\x0b\x32\x19.AcFunDanmu.Im.Basic.User\x12\x11\n\tgroupName\x18\x02 \x01(\t\x12\x14\n\x0cgroupHeadUrl\x18\x03 \x01(\t\x12\x37\n\x08location\x18\x04 \x01(\x0b\x32%.AcFunDanmu.Im.Cloud.Message.Location\x12\x0b\n\x03tag\x18\x05 \x01(\t\x12\x39\n\tgroupType\x18\x06 \x01(\x0e\x32&.AcFunDanmu.Im.Cloud.Message.GroupType\x12\x14\n\x0cintroduction\x18\x07 \x01(\t\x12\x16\n\x0eoriginalTarget\x18\x08 \x01(\t\x12\x36\n\x05label\x18\t \x03(\x0b\x32\'.AcFunDanmu.Im.Cloud.Message.GroupLabelb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'GroupCreateRequest_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GROUPCREATEREQUEST._serialized_start=121
  _GROUPCREATEREQUEST._serialized_end=457
# @@protoc_insertion_point(module_scope)
