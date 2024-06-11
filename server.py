import grpc
from concurrent import futures

from config.middleware import JWTInterceptor
from generated import userauth_pb2_grpc
from services.user_service import UserService
from services.auth_service import AuthService
from config.database import Base, engine


def create_grpc_server() -> grpc.Server:
    Base.metadata.create_all(bind=engine)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), interceptors=[JWTInterceptor()])
    userauth_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    userauth_pb2_grpc.add_AuthServiceServicer_to_server(AuthService(), server)
    return server


def server() -> None:
    init_server = create_grpc_server()
    init_server.add_insecure_port('[::]:50051')
    init_server.start()
    init_server.wait_for_termination()


if __name__ == '__main__':
    server()
