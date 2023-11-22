# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tedapi.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tedapi.proto',
  package='tedapi',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0ctedapi.proto\x12\x06tedapi\"U\n\rParentMessage\x12(\n\x07message\x18\x01 \x01(\x0b\x32\x17.tedapi.MessageEnvelope\x12\x1a\n\x04tail\x18\x02 \x01(\x0b\x32\x0c.tedapi.Tail\"\xe0\x01\n\x0fMessageEnvelope\x12\x17\n\x0f\x64\x65liveryChannel\x18\x01 \x01(\x05\x12#\n\x06sender\x18\x02 \x01(\x0b\x32\x13.tedapi.Participant\x12&\n\trecipient\x18\x03 \x01(\x0b\x32\x13.tedapi.Participant\x12\'\n\x06\x63onfig\x18\x0f \x01(\x0b\x32\x12.tedapi.ConfigTypeH\x00\x88\x01\x01\x12\'\n\x07payload\x18\x10 \x01(\x0b\x32\x11.tedapi.QueryTypeH\x01\x88\x01\x01\x42\t\n\x07_configB\n\n\x08_payload\"g\n\x0bParticipant\x12\r\n\x03\x64in\x18\x01 \x01(\tH\x00\x12\x16\n\x0cteslaService\x18\x02 \x01(\x05H\x00\x12\x0f\n\x05local\x18\x03 \x01(\x05H\x00\x12\x1a\n\x10\x61uthorizedClient\x18\x04 \x01(\x05H\x00\x42\x04\n\x02id\"\x15\n\x04Tail\x12\r\n\x05value\x18\x01 \x01(\x05\"t\n\tQueryType\x12+\n\x04send\x18\x01 \x01(\x0b\x32\x18.tedapi.PayloadQuerySendH\x00\x88\x01\x01\x12(\n\x04recv\x18\x02 \x01(\x0b\x32\x15.tedapi.PayloadStringH\x01\x88\x01\x01\x42\x07\n\x05_sendB\x07\n\x05_recv\"\xac\x01\n\x10PayloadQuerySend\x12\x10\n\x03num\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12+\n\x07payload\x18\x02 \x01(\x0b\x32\x15.tedapi.PayloadStringH\x01\x88\x01\x01\x12\x11\n\x04\x63ode\x18\x03 \x01(\x0cH\x02\x88\x01\x01\x12#\n\x01\x62\x18\x04 \x01(\x0b\x32\x13.tedapi.StringValueH\x03\x88\x01\x01\x42\x06\n\x04_numB\n\n\x08_payloadB\x07\n\x05_codeB\x04\n\x02_b\"z\n\nConfigType\x12,\n\x04send\x18\x01 \x01(\x0b\x32\x19.tedapi.PayloadConfigSendH\x00\x88\x01\x01\x12,\n\x04recv\x18\x02 \x01(\x0b\x32\x19.tedapi.PayloadConfigRecvH\x01\x88\x01\x01\x42\x07\n\x05_sendB\x07\n\x05_recv\"8\n\x11PayloadConfigSend\x12#\n\x04\x66ile\x18\x01 \x01(\x0b\x32\x15.tedapi.PayloadString\"E\n\x11PayloadConfigRecv\x12\"\n\x04\x66ile\x18\x01 \x01(\x0b\x32\x14.tedapi.ConfigString\x12\x0c\n\x04\x63ode\x18\x02 \x01(\x0c\"*\n\x0c\x43onfigString\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x64 \x01(\t\",\n\rPayloadString\x12\r\n\x05value\x18\x01 \x01(\x05\x12\x0c\n\x04text\x18\x02 \x01(\t\"\x1c\n\x0bStringValue\x12\r\n\x05value\x18\x01 \x01(\tb\x06proto3'
)




_PARENTMESSAGE = _descriptor.Descriptor(
  name='ParentMessage',
  full_name='tedapi.ParentMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='tedapi.ParentMessage.message', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tail', full_name='tedapi.ParentMessage.tail', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=109,
)


_MESSAGEENVELOPE = _descriptor.Descriptor(
  name='MessageEnvelope',
  full_name='tedapi.MessageEnvelope',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='deliveryChannel', full_name='tedapi.MessageEnvelope.deliveryChannel', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sender', full_name='tedapi.MessageEnvelope.sender', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='recipient', full_name='tedapi.MessageEnvelope.recipient', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='config', full_name='tedapi.MessageEnvelope.config', index=3,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payload', full_name='tedapi.MessageEnvelope.payload', index=4,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_config', full_name='tedapi.MessageEnvelope._config',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_payload', full_name='tedapi.MessageEnvelope._payload',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=112,
  serialized_end=336,
)


_PARTICIPANT = _descriptor.Descriptor(
  name='Participant',
  full_name='tedapi.Participant',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='din', full_name='tedapi.Participant.din', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='teslaService', full_name='tedapi.Participant.teslaService', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='local', full_name='tedapi.Participant.local', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='authorizedClient', full_name='tedapi.Participant.authorizedClient', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='id', full_name='tedapi.Participant.id',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=338,
  serialized_end=441,
)


_TAIL = _descriptor.Descriptor(
  name='Tail',
  full_name='tedapi.Tail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='tedapi.Tail.value', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=443,
  serialized_end=464,
)


_QUERYTYPE = _descriptor.Descriptor(
  name='QueryType',
  full_name='tedapi.QueryType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='send', full_name='tedapi.QueryType.send', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='recv', full_name='tedapi.QueryType.recv', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_send', full_name='tedapi.QueryType._send',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_recv', full_name='tedapi.QueryType._recv',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=466,
  serialized_end=582,
)


_PAYLOADQUERYSEND = _descriptor.Descriptor(
  name='PayloadQuerySend',
  full_name='tedapi.PayloadQuerySend',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='num', full_name='tedapi.PayloadQuerySend.num', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payload', full_name='tedapi.PayloadQuerySend.payload', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='code', full_name='tedapi.PayloadQuerySend.code', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='b', full_name='tedapi.PayloadQuerySend.b', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_num', full_name='tedapi.PayloadQuerySend._num',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_payload', full_name='tedapi.PayloadQuerySend._payload',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_code', full_name='tedapi.PayloadQuerySend._code',
      index=2, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_b', full_name='tedapi.PayloadQuerySend._b',
      index=3, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=585,
  serialized_end=757,
)


_CONFIGTYPE = _descriptor.Descriptor(
  name='ConfigType',
  full_name='tedapi.ConfigType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='send', full_name='tedapi.ConfigType.send', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='recv', full_name='tedapi.ConfigType.recv', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='_send', full_name='tedapi.ConfigType._send',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
    _descriptor.OneofDescriptor(
      name='_recv', full_name='tedapi.ConfigType._recv',
      index=1, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=759,
  serialized_end=881,
)


_PAYLOADCONFIGSEND = _descriptor.Descriptor(
  name='PayloadConfigSend',
  full_name='tedapi.PayloadConfigSend',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='file', full_name='tedapi.PayloadConfigSend.file', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=883,
  serialized_end=939,
)


_PAYLOADCONFIGRECV = _descriptor.Descriptor(
  name='PayloadConfigRecv',
  full_name='tedapi.PayloadConfigRecv',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='file', full_name='tedapi.PayloadConfigRecv.file', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='code', full_name='tedapi.PayloadConfigRecv.code', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=941,
  serialized_end=1010,
)


_CONFIGSTRING = _descriptor.Descriptor(
  name='ConfigString',
  full_name='tedapi.ConfigString',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='tedapi.ConfigString.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='text', full_name='tedapi.ConfigString.text', index=1,
      number=100, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1012,
  serialized_end=1054,
)


_PAYLOADSTRING = _descriptor.Descriptor(
  name='PayloadString',
  full_name='tedapi.PayloadString',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='tedapi.PayloadString.value', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='text', full_name='tedapi.PayloadString.text', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1056,
  serialized_end=1100,
)


_STRINGVALUE = _descriptor.Descriptor(
  name='StringValue',
  full_name='tedapi.StringValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='tedapi.StringValue.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1102,
  serialized_end=1130,
)

_PARENTMESSAGE.fields_by_name['message'].message_type = _MESSAGEENVELOPE
_PARENTMESSAGE.fields_by_name['tail'].message_type = _TAIL
_MESSAGEENVELOPE.fields_by_name['sender'].message_type = _PARTICIPANT
_MESSAGEENVELOPE.fields_by_name['recipient'].message_type = _PARTICIPANT
_MESSAGEENVELOPE.fields_by_name['config'].message_type = _CONFIGTYPE
_MESSAGEENVELOPE.fields_by_name['payload'].message_type = _QUERYTYPE
_MESSAGEENVELOPE.oneofs_by_name['_config'].fields.append(
  _MESSAGEENVELOPE.fields_by_name['config'])
_MESSAGEENVELOPE.fields_by_name['config'].containing_oneof = _MESSAGEENVELOPE.oneofs_by_name['_config']
_MESSAGEENVELOPE.oneofs_by_name['_payload'].fields.append(
  _MESSAGEENVELOPE.fields_by_name['payload'])
_MESSAGEENVELOPE.fields_by_name['payload'].containing_oneof = _MESSAGEENVELOPE.oneofs_by_name['_payload']
_PARTICIPANT.oneofs_by_name['id'].fields.append(
  _PARTICIPANT.fields_by_name['din'])
_PARTICIPANT.fields_by_name['din'].containing_oneof = _PARTICIPANT.oneofs_by_name['id']
_PARTICIPANT.oneofs_by_name['id'].fields.append(
  _PARTICIPANT.fields_by_name['teslaService'])
_PARTICIPANT.fields_by_name['teslaService'].containing_oneof = _PARTICIPANT.oneofs_by_name['id']
_PARTICIPANT.oneofs_by_name['id'].fields.append(
  _PARTICIPANT.fields_by_name['local'])
_PARTICIPANT.fields_by_name['local'].containing_oneof = _PARTICIPANT.oneofs_by_name['id']
_PARTICIPANT.oneofs_by_name['id'].fields.append(
  _PARTICIPANT.fields_by_name['authorizedClient'])
_PARTICIPANT.fields_by_name['authorizedClient'].containing_oneof = _PARTICIPANT.oneofs_by_name['id']
_QUERYTYPE.fields_by_name['send'].message_type = _PAYLOADQUERYSEND
_QUERYTYPE.fields_by_name['recv'].message_type = _PAYLOADSTRING
_QUERYTYPE.oneofs_by_name['_send'].fields.append(
  _QUERYTYPE.fields_by_name['send'])
_QUERYTYPE.fields_by_name['send'].containing_oneof = _QUERYTYPE.oneofs_by_name['_send']
_QUERYTYPE.oneofs_by_name['_recv'].fields.append(
  _QUERYTYPE.fields_by_name['recv'])
_QUERYTYPE.fields_by_name['recv'].containing_oneof = _QUERYTYPE.oneofs_by_name['_recv']
_PAYLOADQUERYSEND.fields_by_name['payload'].message_type = _PAYLOADSTRING
_PAYLOADQUERYSEND.fields_by_name['b'].message_type = _STRINGVALUE
_PAYLOADQUERYSEND.oneofs_by_name['_num'].fields.append(
  _PAYLOADQUERYSEND.fields_by_name['num'])
_PAYLOADQUERYSEND.fields_by_name['num'].containing_oneof = _PAYLOADQUERYSEND.oneofs_by_name['_num']
_PAYLOADQUERYSEND.oneofs_by_name['_payload'].fields.append(
  _PAYLOADQUERYSEND.fields_by_name['payload'])
_PAYLOADQUERYSEND.fields_by_name['payload'].containing_oneof = _PAYLOADQUERYSEND.oneofs_by_name['_payload']
_PAYLOADQUERYSEND.oneofs_by_name['_code'].fields.append(
  _PAYLOADQUERYSEND.fields_by_name['code'])
_PAYLOADQUERYSEND.fields_by_name['code'].containing_oneof = _PAYLOADQUERYSEND.oneofs_by_name['_code']
_PAYLOADQUERYSEND.oneofs_by_name['_b'].fields.append(
  _PAYLOADQUERYSEND.fields_by_name['b'])
_PAYLOADQUERYSEND.fields_by_name['b'].containing_oneof = _PAYLOADQUERYSEND.oneofs_by_name['_b']
_CONFIGTYPE.fields_by_name['send'].message_type = _PAYLOADCONFIGSEND
_CONFIGTYPE.fields_by_name['recv'].message_type = _PAYLOADCONFIGRECV
_CONFIGTYPE.oneofs_by_name['_send'].fields.append(
  _CONFIGTYPE.fields_by_name['send'])
_CONFIGTYPE.fields_by_name['send'].containing_oneof = _CONFIGTYPE.oneofs_by_name['_send']
_CONFIGTYPE.oneofs_by_name['_recv'].fields.append(
  _CONFIGTYPE.fields_by_name['recv'])
_CONFIGTYPE.fields_by_name['recv'].containing_oneof = _CONFIGTYPE.oneofs_by_name['_recv']
_PAYLOADCONFIGSEND.fields_by_name['file'].message_type = _PAYLOADSTRING
_PAYLOADCONFIGRECV.fields_by_name['file'].message_type = _CONFIGSTRING
DESCRIPTOR.message_types_by_name['ParentMessage'] = _PARENTMESSAGE
DESCRIPTOR.message_types_by_name['MessageEnvelope'] = _MESSAGEENVELOPE
DESCRIPTOR.message_types_by_name['Participant'] = _PARTICIPANT
DESCRIPTOR.message_types_by_name['Tail'] = _TAIL
DESCRIPTOR.message_types_by_name['QueryType'] = _QUERYTYPE
DESCRIPTOR.message_types_by_name['PayloadQuerySend'] = _PAYLOADQUERYSEND
DESCRIPTOR.message_types_by_name['ConfigType'] = _CONFIGTYPE
DESCRIPTOR.message_types_by_name['PayloadConfigSend'] = _PAYLOADCONFIGSEND
DESCRIPTOR.message_types_by_name['PayloadConfigRecv'] = _PAYLOADCONFIGRECV
DESCRIPTOR.message_types_by_name['ConfigString'] = _CONFIGSTRING
DESCRIPTOR.message_types_by_name['PayloadString'] = _PAYLOADSTRING
DESCRIPTOR.message_types_by_name['StringValue'] = _STRINGVALUE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ParentMessage = _reflection.GeneratedProtocolMessageType('ParentMessage', (_message.Message,), {
  'DESCRIPTOR' : _PARENTMESSAGE,
  '__module__' : 'tedapi_pb2'
  # @@protoc_insertion_point(class_scope:tedapi.ParentMessage)
  })
_sym_db.RegisterMessage(ParentMessage)

MessageEnvelope = _reflection.GeneratedProtocolMessageType('MessageEnvelope', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGEENVELOPE,
  '__module__' : 'tedapi_pb2'
  # @@protoc_insertion_point(class_scope:tedapi.MessageEnvelope)
  })
_sym_db.RegisterMessage(MessageEnvelope)

Participant = _reflection.GeneratedProtocolMessageType('Participant', (_message.Message,), {
  'DESCRIPTOR' : _PARTICIPANT,
  '__module__' : 'tedapi_pb2'
  # @@protoc_insertion_point(class_scope:tedapi.Participant)
  })
_sym_db.RegisterMessage(Participant)

Tail = _reflection.GeneratedProtocolMessageType('Tail', (_message.Message,), {
  'DESCRIPTOR' : _TAIL,
  '__module__' : 'tedapi_pb2'
  # @@protoc_insertion_point(class_scope:tedapi.Tail)
  })
_sym_db.RegisterMessage(Tail)

QueryType = _reflection.GeneratedProtocolMessageType('QueryType', (_message.Message,), {
  'DESCRIPTOR' : _QUERYTYPE,
  '__module__' : 'tedapi_pb2'
  # @@protoc_insertion_point(class_scope:tedapi.QueryType)
  })
_sym_db.RegisterMessage(QueryType)

PayloadQuerySend = _reflection.GeneratedProtocolMessageType('PayloadQuerySend', (_message.Message,), {
  'DESCRIPTOR' : _PAYLOADQUERYSEND,
  '__module__' : 'tedapi_pb2'
  # @@protoc_insertion_point(class_scope:tedapi.PayloadQuerySend)
  })
_sym_db.RegisterMessage(PayloadQuerySend)

ConfigType = _reflection.GeneratedProtocolMessageType('ConfigType', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGTYPE,
  '__module__' : 'tedapi_pb2'
  # @@protoc_insertion_point(class_scope:tedapi.ConfigType)
  })
_sym_db.RegisterMessage(ConfigType)

PayloadConfigSend = _reflection.GeneratedProtocolMessageType('PayloadConfigSend', (_message.Message,), {
  'DESCRIPTOR' : _PAYLOADCONFIGSEND,
  '__module__' : 'tedapi_pb2'
  # @@protoc_insertion_point(class_scope:tedapi.PayloadConfigSend)
  })
_sym_db.RegisterMessage(PayloadConfigSend)

PayloadConfigRecv = _reflection.GeneratedProtocolMessageType('PayloadConfigRecv', (_message.Message,), {
  'DESCRIPTOR' : _PAYLOADCONFIGRECV,
  '__module__' : 'tedapi_pb2'
  # @@protoc_insertion_point(class_scope:tedapi.PayloadConfigRecv)
  })
_sym_db.RegisterMessage(PayloadConfigRecv)

ConfigString = _reflection.GeneratedProtocolMessageType('ConfigString', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGSTRING,
  '__module__' : 'tedapi_pb2'
  # @@protoc_insertion_point(class_scope:tedapi.ConfigString)
  })
_sym_db.RegisterMessage(ConfigString)

PayloadString = _reflection.GeneratedProtocolMessageType('PayloadString', (_message.Message,), {
  'DESCRIPTOR' : _PAYLOADSTRING,
  '__module__' : 'tedapi_pb2'
  # @@protoc_insertion_point(class_scope:tedapi.PayloadString)
  })
_sym_db.RegisterMessage(PayloadString)

StringValue = _reflection.GeneratedProtocolMessageType('StringValue', (_message.Message,), {
  'DESCRIPTOR' : _STRINGVALUE,
  '__module__' : 'tedapi_pb2'
  # @@protoc_insertion_point(class_scope:tedapi.StringValue)
  })
_sym_db.RegisterMessage(StringValue)


# @@protoc_insertion_point(module_scope)
