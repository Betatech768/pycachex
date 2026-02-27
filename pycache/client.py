import socket

def client():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.connect(("127.0.0.1", 12345))
        print("Connected to server. Type 'quit' to stop")

        while True:
            message = input("Message to Send: ")
            if message.lower() == 'quit': break
            server.sendall(message.encode())
            data = server.recv(1024)

    except KeyboardInterrupt:
        print("\nServer closed")
    finally:
        server.close()

if __name__ == "__main__":
    client()