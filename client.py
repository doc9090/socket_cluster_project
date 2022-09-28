import socket

IP=socket.gethostname()
PORT=53
ADDR=(IP,PORT)
FORMAT="utf-8"
SIZE=1024

def main():
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(ADDR)
        