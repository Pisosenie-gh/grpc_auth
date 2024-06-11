import grpc
from pydantic_core._pydantic_core import ValidationError
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound

from config.database import get_db
import generated.userauth_pb2 as userauth_pb2
import generated.userauth_pb2_grpc as userauth_pb2_grpc
from utils.password import get_password_hash, pwd_context

from utils.jwt import generate_access_token, generate_refresh_token, verify_token

from schemas.auth import LoginSchema, LoginPasswordValidator

from controllers.user import UserController


class AuthService(userauth_pb2_grpc.AuthServiceServicer, UserController):
    def Login(self, request: userauth_pb2.AuthRequest, context: grpc.ServicerContext) -> userauth_pb2.AuthResponse:
        db: Session = next(get_db())

        email = request.email
        password = request.password
        try:
            data = LoginSchema(email=email, password=password)
            db_user = self.get_user_by_email(email)
            password_validation = LoginPasswordValidator(password=password, db_password=db_user.password)
        except ValidationError as e:
            context.abort(grpc.StatusCode.UNAUTHENTICATED, str(e))
        except NoResultFound:
            context.abort(grpc.StatusCode.NOT_FOUND)
        access_token = generate_access_token(db_user.id)
        refresh_token = generate_refresh_token(db_user.id)
        response = userauth_pb2.AuthResponse(access_token=access_token, refresh_token=refresh_token)
        return response

    def RefreshToken(self, request: userauth_pb2.RefreshTokenRequest,
                     context: grpc.ServicerContext) -> userauth_pb2.AuthResponse:
        try:
            user_id = verify_token(request.refresh_token)
            access_token = generate_access_token(user_id)
            refresh_token = generate_refresh_token(user_id)
            response = userauth_pb2.AuthResponse(access_token=access_token, refresh_token=refresh_token)
            return response
        except Exception as e:
            context.abort(grpc.StatusCode.UNAUTHENTICATED, str(e))

    def ValidateToken(self, request: userauth_pb2.AuthResponse, context: grpc.ServicerContext) -> userauth_pb2.Empty:
        try:
            verify_token(request.token)
            return userauth_pb2.Empty()
        except Exception as e:
            context.abort(grpc.StatusCode.UNAUTHENTICATED, str(e))
