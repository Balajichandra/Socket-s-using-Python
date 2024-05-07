import socket
clinet_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clinet_socket.connect(('127.0.0.1',12345))
payload = "Hey Server..."

try:
    while True:
        clinet_socket.send(payload.encode('utf-8'))
        data = clinet_socket.recv(1024)
        print(str(data))
        more = input("Do you want to send more data to client...")
        if more.lower() =='y':
            payload = input("Enter payload")
        else:
            break    
except KeyboardInterrupt:
    print("Exicted by user:")
clinet_socket.close()    