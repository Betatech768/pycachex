import socket

def create_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('127.0.0.1', 12345))
        s.listen()
        print(f"Server is Listening...")

        conn, addr = s.accept()

        with conn:
            print(f"Server Started on Port 12345")

            while True:
                data = conn.recv(1024)
                if not data: break
                conn.send(data)
