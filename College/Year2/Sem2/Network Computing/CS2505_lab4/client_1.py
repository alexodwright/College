import sys
import socket

dns, filename = sys.argv[1], sys.argv[2]

with open(filename) as file:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for line in file:
        client_socket.sendto(line.encode(), (dns, 6789))
    res = client_socket.recv(128).decode()
    while res:
        print(res) 
        res = client_socket.recv(128).decode()
client_socket.close()

