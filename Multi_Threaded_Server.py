import socket
from _thread import *

server_socket = socket.socket()
host = "127.0.0.1"
port = 1233
ThreadCount = 0

try:
    server_socket.bind((host,port))
except socket.error as e:
    print(str(e))

print("Wating for connection...")
server_socket.listen(5)

def clinet_thread(connection):
    connection.send(str.encode("Welcome to the server..."))
    while True:
        data = connection.recv(2048)
        reply = "Hello I am a Server"+data.decode("utf-8")
        if not data:
            break
        connection.sendall(str.encode(reply))
    connection.close()
while True:
    client,addr = server_socket.accept()
    print("Connection to"+addr[0]+str(addr[1]))
    start_new_thread(clinet_thread,(client,))
    ThreadCount+=1
    print("ThreadNumber:"+str(ThreadCount))
server_socket.close()            