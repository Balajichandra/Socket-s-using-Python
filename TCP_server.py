import socket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1',12345))
server_socket.listen(5) #max no of connection it can connect

while True:
    print("Server waiting for connection...")
    cline_socket,addr = server_socket.accept()
    print("Clinet connected from:",addr)
    while True: # recive data from clinet
        data = cline_socket.recv(1024)#1024 is buffer size in bytes
        if not data or data.decode('utf-8') == 'END':
            break
        print("received from client client:%s" % data.decode("utf-8"))
        try: #send data to client
            cline_socket.send(bytes('Hey Client','utf-8'))
        except:
            print("Exited by the user...")
    cline_socket.close()
server_socket.close()                