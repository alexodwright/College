import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("", 6789))
print("Receiving...")
while True:
    message, client_addr = server_socket.recvfrom(2048)
    print(f"Received: {message.decode()}")
    message = message.upper()
    server_socket.sendto(message, client_addr)
server_socket.close()
