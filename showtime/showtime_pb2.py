# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: showtime.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eshowtime.proto\"\x14\n\x04\x44\x61te\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\"\x16\n\x05Movie\x12\r\n\x05movie\x18\x01 \x01(\t\"\'\n\x08Schedule\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\r\n\x05movie\x18\x02 \x03(\t\"\x07\n\x05\x45mpty2N\n\x08Showtime\x12\"\n\x0fGetMoviesByDate\x12\x05.Date\x1a\x06.Movie\"\x00\x12\x1e\n\x08GetTimes\x12\x06.Empty\x1a\x06.Movie\"\x00\x30\x01\x62\x06proto3')



_DATE = DESCRIPTOR.message_types_by_name['Date']
_MOVIE = DESCRIPTOR.message_types_by_name['Movie']
_SCHEDULE = DESCRIPTOR.message_types_by_name['Schedule']
_EMPTY = DESCRIPTOR.message_types_by_name['Empty']
Date = _reflection.GeneratedProtocolMessageType('Date', (_message.Message,), {
  'DESCRIPTOR' : _DATE,
  '__module__' : 'showtime_pb2'
  # @@protoc_insertion_point(class_scope:Date)
  })
_sym_db.RegisterMessage(Date)

Movie = _reflection.GeneratedProtocolMessageType('Movie', (_message.Message,), {
  'DESCRIPTOR' : _MOVIE,
  '__module__' : 'showtime_pb2'
  # @@protoc_insertion_point(class_scope:Movie)
  })
_sym_db.RegisterMessage(Movie)

Schedule = _reflection.GeneratedProtocolMessageType('Schedule', (_message.Message,), {
  'DESCRIPTOR' : _SCHEDULE,
  '__module__' : 'showtime_pb2'
  # @@protoc_insertion_point(class_scope:Schedule)
  })
_sym_db.RegisterMessage(Schedule)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'showtime_pb2'
  # @@protoc_insertion_point(class_scope:Empty)
  })
_sym_db.RegisterMessage(Empty)

_SHOWTIME = DESCRIPTOR.services_by_name['Showtime']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DATE._serialized_start=18
  _DATE._serialized_end=38
  _MOVIE._serialized_start=40
  _MOVIE._serialized_end=62
  _SCHEDULE._serialized_start=64
  _SCHEDULE._serialized_end=103
  _EMPTY._serialized_start=105
  _EMPTY._serialized_end=112
  _SHOWTIME._serialized_start=114
  _SHOWTIME._serialized_end=192
# @@protoc_insertion_point(module_scope)
