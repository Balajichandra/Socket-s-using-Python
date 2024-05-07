import socket
clinet_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

msg = "Hello UDP Server"
clinet_socket.sendto(msg.encode("utf-8"),('127.0.0.1',12345))
data,addr = clinet_socket.recvfrom(4096)
print("Server says...")
print(str(data))
clinet_socket.close()