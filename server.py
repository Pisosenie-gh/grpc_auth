from setup import create_grpc_server


def server() -> None:
    init_server = create_grpc_server()
    init_server.add_insecure_port('[::]:50051')
    init_server.start()
    init_server.wait_for_termination()


if __name__ == '__main__':
    server()
