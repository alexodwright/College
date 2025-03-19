import sys
import socket

dns, filename = sys.argv[1], sys.argv[2]

with open(filename) as file:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for line in file:
        client_socket.sendto(line.encode(), (dns, 6789))
        res = client_socket.recv(len(line.encode())).decode()
        print("Res: " + res)
    client_socket.close()