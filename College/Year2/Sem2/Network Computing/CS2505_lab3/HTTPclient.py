import sys
import socket

server_host, server_port, filename = sys.argv[1], sys.argv[2], sys.argv[3]
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_host, int(server_port)))
request = f"GET /{filename} HTTP/1.1\nHost: {server_host}:{server_port}"
request = request.encode()
client_socket.sendall(request)
data = client_socket.recv(1024).decode()
while data != "":
    print(data, end="")
    data = client_socket.recv(1024).decode()
client_socket.close()


