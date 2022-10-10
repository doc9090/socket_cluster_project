import socket
import re


IP="localhost"
PORT=53
ADDR=(IP,PORT)
FORMAT="utf-8"
SIZE=1024
passw="1234"
msg_server="Password is correct"

def main():
    print("Connection starting...")
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print("Server listening...")
    
    conn,addr=server.accept()
    print(f"New connection with {addr}")

    conn.send(passw.encode(FORMAT))
    received_pss=str(conn.recv(SIZE).decode(FORMAT))

    if received_pss == passw:

        conn.send(msg_server.encode(FORMAT))

        condt=""
        
        while condt != "exit":
        
            msg_send_loop="Message received is : "

            filename=conn.recv(SIZE).decode(FORMAT)

            condt=str(filename)
            print(condt)

            msg_f_send=msg_send_loop+condt
            
            conn.send(msg_f_send.encode(FORMAT))

            if condt=="help":

                message_to_help=" -> I will illustrate what I can do for you: "

                conn.send(message_to_help.encode(FORMAT))


            
            
            if condt=="count":

                message_count=" -> Well, tell me your sentence, I will provide you the number of words..."

                conn.send(message_count.encode(FORMAT))

                sent_to_count=conn.recv(SIZE).decode(FORMAT)
                s_t_c=str(sent_to_count)
                send_count=str(count_words(s_t_c))

                message_counter="Your sentence is composed by : " +send_count + " words"

                conn.send(message_counter.encode(FORMAT))
                
                
                
                print(send_count)

            
            






def count_words(sentence):

    number_words=len(re.findall(r'\w+',sentence))

    print(number_words)
    return number_words
        


main()