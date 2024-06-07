import grpc
from concurrent import futures
from generated import userauth_pb2_grpc
from services.user_service import UserService
from services.auth_service import AuthService
from config.database import Base, engine


def create_grpc_server() -> grpc.Server:
    Base.metadata.create_all(bind=engine)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    userauth_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    userauth_pb2_grpc.add_AuthServiceServicer_to_server(AuthService(), server)
    return server
