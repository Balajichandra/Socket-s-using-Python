import socket
clinet_socket = socket.socket()
host = "127.0.0.1"
port = 1233

print("Wating for connection...")
try:
    clinet_socket.connect((host,port))
except socket.error as e:
    print(str(e))

Response = clinet_socket.recv(1024)
print(Response.decode('utf-8'))
while True:
    Input = input("Say Something...")
    clinet_socket.send(str.encode(Input))
    response = clinet_socket.recv(1024)
    print(response.decode("utf-8"))
clinet_socket.close()    