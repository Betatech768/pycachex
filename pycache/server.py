import socket
import threading


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")
    with conn:
        while True:
            try:
                data = conn.recv(1024)
                if not data:
                    break
            except ConnectionResetError:
                break
    print(f"[DISCONNECTED {addr} left.")



def create_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    with server as server:
        server.bind(("127.0.0.1", 12345))
        server.listen()
        print(f"Server Listening... ")

        try:
            while True:
                conn, addr = server.accept()
                thread = threading.Thread(target=handle_client, args=(conn, addr))
                thread.start()
        except ConnectionResetError as e:
            print(f" Error occurred {e}")


if __name__ == "__main__":
    create_server()