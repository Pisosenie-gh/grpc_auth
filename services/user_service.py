import grpc
from controllers.user import UserController
import generated.userauth_pb2 as userauth_pb2
import generated.userauth_pb2_grpc as userauth_pb2_grpc
from pydantic import ValidationError
from schemas.user import UserCreate, UserUpdate, ChangePassword, UserDelete, UserGet


class UserService(userauth_pb2_grpc.UserServiceServicer, UserController):

    def CreateUser(self, request: userauth_pb2.User, context: grpc.ServicerContext) -> userauth_pb2.UserResponse:
        try:
            user_data = UserCreate(name=request.name, email=request.email, password=request.password)
        except ValidationError as e:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, str(e))

        if self.get_user_by_email(request.email):
            context.abort(grpc.StatusCode.ALREADY_EXISTS, "Email already registered")

        db_user = self.create_user(**user_data.dict())
        return userauth_pb2.UserResponse(
            id=str(db_user.id),
            name=db_user.name,
            email=db_user.email,
        )

    def GetUser(self, request: userauth_pb2.User, context: grpc.ServicerContext) -> userauth_pb2.UserResponse:
        try:
            user_data = UserGet(id=request.id)
        except ValidationError as e:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, str(e))
        db_user = self.get_user(request.email, request.id)
        return userauth_pb2.UserResponse(
            id=str(db_user.id),
            name=db_user.name,
            email=db_user.email,
        )

    def UpdateUser(self, request: userauth_pb2.EditUserRequest,
                   context: grpc.ServicerContext) -> userauth_pb2.UserResponse:
        try:
            user_data = UserUpdate(name=request.name, email=request.email, id=request.id)
        except ValidationError as e:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, str(e))

        db_user = self.update_user(**user_data.dict())
        return userauth_pb2.UserResponse(
            id=str(db_user.id),
            name=db_user.name,
            email=db_user.email,
        )

    def ChangePassword(self, request: userauth_pb2.ChangePasswordRequest,
                       context: grpc.ServicerContext) -> userauth_pb2.Empty:
        try:
            user_data = ChangePassword(id=request.id, old_password=request.old_password,
                                       new_password=request.new_password)
        except ValidationError as e:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, str(e))

        self.change_password(**user_data.dict())
        return userauth_pb2.Empty()

    def DeleteUser(self, request: userauth_pb2.DeleteUserRequest, context: grpc.ServicerContext) -> userauth_pb2.Empty:
        try:
            user_data = UserDelete(id=request.id)
        except ValidationError as e:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, str(e))
        self.delete_user(**user_data.dict())
        return userauth_pb2.Empty()
