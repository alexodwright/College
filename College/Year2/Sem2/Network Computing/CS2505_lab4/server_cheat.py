import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("", 6789))
print("Receiving...")

while True:
    message, client_addr = server_socket.recvfrom(2048)
    print(f"Received: {message.decode().strip()}")
    
    if message.decode().strip() == "END":
        print("Termination message received. Closing server.")
        server_socket.sendto(b"ACK", client_addr)
        break
    
    # Process the message (in this case, convert to uppercase)
    processed_message = message.upper()
    
    # Send acknowledgment
    server_socket.sendto(b"ACK", client_addr)
    print(f"Sent ACK for: {processed_message.decode().strip()}")

server_socket.close()
