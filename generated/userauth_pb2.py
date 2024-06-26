# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/userauth.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14proto/userauth.proto\x12\x08userauth\"A\n\x04User\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x10\n\x08password\x18\x04 \x01(\t\"7\n\x0cUserResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\".\n\x0b\x41uthRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\";\n\x0c\x41uthResponse\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\x12\x15\n\rrefresh_token\x18\x02 \x01(\t\",\n\x13RefreshTokenRequest\x12\x15\n\rrefresh_token\x18\x01 \x01(\t\"O\n\x15\x43hangePasswordRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0cold_password\x18\x02 \x01(\t\x12\x14\n\x0cnew_password\x18\x03 \x01(\t\":\n\x0f\x45\x64itUserRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\"\x1f\n\x11\x44\x65leteUserRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\x07\n\x05\x45mpty2\xb7\x02\n\x0bUserService\x12\x34\n\nCreateUser\x12\x0e.userauth.User\x1a\x16.userauth.UserResponse\x12\x31\n\x07GetUser\x12\x0e.userauth.User\x1a\x16.userauth.UserResponse\x12?\n\nUpdateUser\x12\x19.userauth.EditUserRequest\x1a\x16.userauth.UserResponse\x12\x42\n\x0e\x43hangePassword\x12\x1f.userauth.ChangePasswordRequest\x1a\x0f.userauth.Empty\x12:\n\nDeleteUser\x12\x1b.userauth.DeleteUserRequest\x1a\x0f.userauth.Empty2\xc6\x01\n\x0b\x41uthService\x12\x36\n\x05Login\x12\x15.userauth.AuthRequest\x1a\x16.userauth.AuthResponse\x12\x38\n\rValidateToken\x12\x16.userauth.AuthResponse\x1a\x0f.userauth.Empty\x12\x45\n\x0cRefreshToken\x12\x1d.userauth.RefreshTokenRequest\x1a\x16.userauth.AuthResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.userauth_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_USER']._serialized_start=34
  _globals['_USER']._serialized_end=99
  _globals['_USERRESPONSE']._serialized_start=101
  _globals['_USERRESPONSE']._serialized_end=156
  _globals['_AUTHREQUEST']._serialized_start=158
  _globals['_AUTHREQUEST']._serialized_end=204
  _globals['_AUTHRESPONSE']._serialized_start=206
  _globals['_AUTHRESPONSE']._serialized_end=265
  _globals['_REFRESHTOKENREQUEST']._serialized_start=267
  _globals['_REFRESHTOKENREQUEST']._serialized_end=311
  _globals['_CHANGEPASSWORDREQUEST']._serialized_start=313
  _globals['_CHANGEPASSWORDREQUEST']._serialized_end=392
  _globals['_EDITUSERREQUEST']._serialized_start=394
  _globals['_EDITUSERREQUEST']._serialized_end=452
  _globals['_DELETEUSERREQUEST']._serialized_start=454
  _globals['_DELETEUSERREQUEST']._serialized_end=485
  _globals['_EMPTY']._serialized_start=487
  _globals['_EMPTY']._serialized_end=494
  _globals['_USERSERVICE']._serialized_start=497
  _globals['_USERSERVICE']._serialized_end=808
  _globals['_AUTHSERVICE']._serialized_start=811
  _globals['_AUTHSERVICE']._serialized_end=1009
# @@protoc_insertion_point(module_scope)
