import grpc
from sqlalchemy.orm import Session
from models.users import User as UserModel
from config.database import get_db
import generated.userauth_pb2 as userauth_pb2
import generated.userauth_pb2_grpc as userauth_pb2_grpc
from utils.password import get_password_hash, pwd_context

from utils.jwt import generate_access_token, generate_refresh_token, verify_token


class AuthService(userauth_pb2_grpc.AuthServiceServicer):
    def Login(self, request: userauth_pb2.AuthRequest, context: grpc.ServicerContext) -> userauth_pb2.AuthResponse:
        db: Session = next(get_db())

        if not request.email or not request.password:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, "Email and password must be provided")

        db_user = db.query(UserModel).filter(UserModel.email == request.email).first()
        if not db_user or not pwd_context.verify(request.password, db_user.password):
            context.abort(grpc.StatusCode.UNAUTHENTICATED, "Invalid credentials")

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
