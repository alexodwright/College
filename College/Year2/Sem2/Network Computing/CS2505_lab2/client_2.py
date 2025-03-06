# from the socket module import all
import socket
# Create a TCP socket using the "socket" method
# Hints: AF_INET is used for IPv4 protocols, SOCK_STREAM is used for TCP
client_socket = socket.socket()
# set values for host 'localhost' - meaning this machine and port number 10000
# the machine address and port number have to be the same as the server is using.
port_number = int(input("Enter in the port number: "))
ip_addr = input("Enter in the ip: ")
server_address = (ip_addr, port_number)
# output to terminal some info on the address details
print('connecting to server at %s port %s' % server_address)
# Connect the socket to the host and port
client_socket.connect(server_address)
while True:
    # Send data
    message = input("Enter a message to send to the server: ")
    print('sending "%s"' % message)
    # Data is transmitted to the server with sendall()
    # encode() function returns bytes object
    client_socket.sendall(message.encode())

    # Look for the response
    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
    	# Data is read from the connection with recv()
        # decode() function returns string object
        data = client_socket.recv(1024).decode()
        amount_received += len(data)
        print('received "%s"' % data)
