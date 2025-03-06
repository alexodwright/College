# from the socket module import all
import socket
# Create a TCP server socket
# Create a TCP socket using the "socket" method
# Hints: AF_INET is used for IPv4 protocols, SOCK_STREAM is used for TCP
server_socket = socket.socket()
# set values for host 'localhost' - meaning this machine and port number 10000
port_number = int(input("Enter in the port number: "))
ip_addr = socket.gethostbyname(socket.gethostname())
print(ip_addr)
server_address = (ip_addr, port_number)
# output to terminal some info on the address details
print('*** Server is starting up on %s port %s ***' % server_address)
# Bind the socket to the host and port
server_socket.bind(server_address)
# Listen for one incoming connections to the server
server_socket.listen(1)

# we want the server to run all the time, so set up a forever true while loop
while True:

    # Now the server waits for a connection
    print('*** Waiting for a connection ***')
    # accept() returns an open connection between the server and client, alongj
    connection, client_address = server_socket.accept()

    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            # decode() function returns string object
            data = connection.recv(16).decode()
            if data:
                print('received "%s"' % data)
                print('sending data back to the client')

                # encode() function returns bytes object
                data = input("Enter a message to send back to the server: ")
                connection.sendall(data.encode())
            else:
                print('no more data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()

# now close the socket
server_socket.close()
