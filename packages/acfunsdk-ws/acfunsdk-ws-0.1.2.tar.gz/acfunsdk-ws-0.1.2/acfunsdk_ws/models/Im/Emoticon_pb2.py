# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Emoticon.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import PicUrl_pb2 as PicUrl__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0e\x45moticon.proto\x12\x1b\x41\x63\x46unDanmu.Im.Cloud.Message\x1a\x0cPicUrl.proto\"\x83\x03\n\x08\x45moticon\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tpackageId\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x38\n\x04type\x18\x04 \x01(\x0e\x32*.AcFunDanmu.Im.Cloud.Message.Emoticon.Type\x12\x33\n\x06\x62igUrl\x18\x05 \x03(\x0b\x32#.AcFunDanmu.Im.Cloud.Message.PicUrl\x12\r\n\x05width\x18\x06 \x01(\x05\x12\x0e\n\x06height\x18\x07 \x01(\x05\x12@\n\x0c\x65moticonCode\x18\x08 \x03(\x0b\x32*.AcFunDanmu.Im.Cloud.Message.Emoticon.Code\x1a&\n\x04\x43ode\x12\x10\n\x08language\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x03(\t\"R\n\x04Type\x12\x0b\n\x07UNKNOWN\x10\x00\x12\t\n\x05\x42\x41SIC\x10\x01\x12\t\n\x05IMAGE\x10\x02\x12\x07\n\x03GIF\x10\x03\x12\x12\n\x0eSPECIAL_EFFECT\x10\x04\x12\n\n\x06SCRIPT\x10\x05\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Emoticon_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EMOTICON._serialized_start=62
  _EMOTICON._serialized_end=449
  _EMOTICON_CODE._serialized_start=327
  _EMOTICON_CODE._serialized_end=365
  _EMOTICON_TYPE._serialized_start=367
  _EMOTICON_TYPE._serialized_end=449
# @@protoc_insertion_point(module_scope)
