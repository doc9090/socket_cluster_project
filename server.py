import socket 

IP="0.0.0.0"
PORT=53
ADDR=(IP,PORT)
FORMAT="utf-8"
SIZE=1024

def main():
    print("Connection starting...")
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print("Server listening...")

    while True:
        conn,addr=server.accept()
        print(f"New connection with {addr}")
        filename=conn.recv(SIZE).decode(FORMAT)
        print(filename)

main()