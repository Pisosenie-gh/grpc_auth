# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from generated import userauth_pb2 as proto_dot_userauth__pb2

GRPC_GENERATED_VERSION = '1.64.1'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in proto/userauth_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class UserServiceStub(object):
    """Сервисы
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateUser = channel.unary_unary(
                '/userauth.UserService/CreateUser',
                request_serializer=proto_dot_userauth__pb2.User.SerializeToString,
                response_deserializer=proto_dot_userauth__pb2.UserResponse.FromString,
                _registered_method=True)
        self.GetUser = channel.unary_unary(
                '/userauth.UserService/GetUser',
                request_serializer=proto_dot_userauth__pb2.User.SerializeToString,
                response_deserializer=proto_dot_userauth__pb2.UserResponse.FromString,
                _registered_method=True)
        self.UpdateUser = channel.unary_unary(
                '/userauth.UserService/UpdateUser',
                request_serializer=proto_dot_userauth__pb2.EditUserRequest.SerializeToString,
                response_deserializer=proto_dot_userauth__pb2.UserResponse.FromString,
                _registered_method=True)
        self.ChangePassword = channel.unary_unary(
                '/userauth.UserService/ChangePassword',
                request_serializer=proto_dot_userauth__pb2.ChangePasswordRequest.SerializeToString,
                response_deserializer=proto_dot_userauth__pb2.Empty.FromString,
                _registered_method=True)
        self.DeleteUser = channel.unary_unary(
                '/userauth.UserService/DeleteUser',
                request_serializer=proto_dot_userauth__pb2.DeleteUserRequest.SerializeToString,
                response_deserializer=proto_dot_userauth__pb2.Empty.FromString,
                _registered_method=True)


class UserServiceServicer(object):
    """Сервисы
    """

    def CreateUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ChangePassword(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateUser,
                    request_deserializer=proto_dot_userauth__pb2.User.FromString,
                    response_serializer=proto_dot_userauth__pb2.UserResponse.SerializeToString,
            ),
            'GetUser': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUser,
                    request_deserializer=proto_dot_userauth__pb2.User.FromString,
                    response_serializer=proto_dot_userauth__pb2.UserResponse.SerializeToString,
            ),
            'UpdateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateUser,
                    request_deserializer=proto_dot_userauth__pb2.EditUserRequest.FromString,
                    response_serializer=proto_dot_userauth__pb2.UserResponse.SerializeToString,
            ),
            'ChangePassword': grpc.unary_unary_rpc_method_handler(
                    servicer.ChangePassword,
                    request_deserializer=proto_dot_userauth__pb2.ChangePasswordRequest.FromString,
                    response_serializer=proto_dot_userauth__pb2.Empty.SerializeToString,
            ),
            'DeleteUser': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteUser,
                    request_deserializer=proto_dot_userauth__pb2.DeleteUserRequest.FromString,
                    response_serializer=proto_dot_userauth__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'userauth.UserService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('userauth.UserService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class UserService(object):
    """Сервисы
    """

    @staticmethod
    def CreateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/userauth.UserService/CreateUser',
            proto_dot_userauth__pb2.User.SerializeToString,
            proto_dot_userauth__pb2.UserResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/userauth.UserService/GetUser',
            proto_dot_userauth__pb2.User.SerializeToString,
            proto_dot_userauth__pb2.UserResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def UpdateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/userauth.UserService/UpdateUser',
            proto_dot_userauth__pb2.EditUserRequest.SerializeToString,
            proto_dot_userauth__pb2.UserResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ChangePassword(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/userauth.UserService/ChangePassword',
            proto_dot_userauth__pb2.ChangePasswordRequest.SerializeToString,
            proto_dot_userauth__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/userauth.UserService/DeleteUser',
            proto_dot_userauth__pb2.DeleteUserRequest.SerializeToString,
            proto_dot_userauth__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)


class AuthServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Login = channel.unary_unary(
                '/userauth.AuthService/Login',
                request_serializer=proto_dot_userauth__pb2.AuthRequest.SerializeToString,
                response_deserializer=proto_dot_userauth__pb2.AuthResponse.FromString,
                _registered_method=True)
        self.ValidateToken = channel.unary_unary(
                '/userauth.AuthService/ValidateToken',
                request_serializer=proto_dot_userauth__pb2.AuthResponse.SerializeToString,
                response_deserializer=proto_dot_userauth__pb2.Empty.FromString,
                _registered_method=True)
        self.RefreshToken = channel.unary_unary(
                '/userauth.AuthService/RefreshToken',
                request_serializer=proto_dot_userauth__pb2.RefreshTokenRequest.SerializeToString,
                response_deserializer=proto_dot_userauth__pb2.AuthResponse.FromString,
                _registered_method=True)


class AuthServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Login(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ValidateToken(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RefreshToken(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AuthServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Login': grpc.unary_unary_rpc_method_handler(
                    servicer.Login,
                    request_deserializer=proto_dot_userauth__pb2.AuthRequest.FromString,
                    response_serializer=proto_dot_userauth__pb2.AuthResponse.SerializeToString,
            ),
            'ValidateToken': grpc.unary_unary_rpc_method_handler(
                    servicer.ValidateToken,
                    request_deserializer=proto_dot_userauth__pb2.AuthResponse.FromString,
                    response_serializer=proto_dot_userauth__pb2.Empty.SerializeToString,
            ),
            'RefreshToken': grpc.unary_unary_rpc_method_handler(
                    servicer.RefreshToken,
                    request_deserializer=proto_dot_userauth__pb2.RefreshTokenRequest.FromString,
                    response_serializer=proto_dot_userauth__pb2.AuthResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'userauth.AuthService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('userauth.AuthService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class AuthService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Login(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/userauth.AuthService/Login',
            proto_dot_userauth__pb2.AuthRequest.SerializeToString,
            proto_dot_userauth__pb2.AuthResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ValidateToken(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/userauth.AuthService/ValidateToken',
            proto_dot_userauth__pb2.AuthResponse.SerializeToString,
            proto_dot_userauth__pb2.Empty.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RefreshToken(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/userauth.AuthService/RefreshToken',
            proto_dot_userauth__pb2.RefreshTokenRequest.SerializeToString,
            proto_dot_userauth__pb2.AuthResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
