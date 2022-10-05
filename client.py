import socket

IP="localhost"
PORT=53
ADDR=(IP,PORT)
FORMAT="utf-8"
SIZE=1024

def main():
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(ADDR)
    cnd_1=""

    passw=str(client.recv(SIZE).decode(FORMAT))
    
    while cnd_1!="exit":

        msg =input("Write a password ")
        client.send(msg.encode(FORMAT))

        if msg==passw:
            
            file_server=client.recv(SIZE).decode(FORMAT)
            print(file_server)
            send_msg(client)
            


        
            
def send_msg(c):
    
    exit_cnd=""
    
    while exit_cnd != "exit":

        msg_client=input("Send a message > ")
        c.send(msg_client.encode(FORMAT))
        
        
        answer_server=c.recv(SIZE).decode(FORMAT)
        print(str(answer_server))
        
        exit_cnd=msg_client

    return exit_cnd
        

main()