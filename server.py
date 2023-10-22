import socket

SERVER = 50000
CLIENT1 = 50001
CLIENT2 = 50002
HOST = socket.gethostbyname(socket.gethostname())
BACKLOG = 50


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, SERVER))
        s.listen(BACKLOG)
        conn, addr = s.accept()
        with conn:
            print(f"connected by {addr}")
        
