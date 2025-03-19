import sys
import socket
import time

dns, filename = sys.argv[1], sys.argv[2]
TIMEOUT = 1  # Timeout in seconds

def send_with_timeout(sock, message, address):
    while True:
        sock.sendto(message, address)
        print(f"Sent: {message.decode().strip()}")
        
        start_time = time.time()
        while time.time() - start_time < TIMEOUT:
            try:
                sock.settimeout(TIMEOUT - (time.time() - start_time))
                response, _ = sock.recvfrom(1024)
                print(f"Received ACK: {response.decode().strip()}")
                return
            except socket.timeout:
                pass
        
        print("Timeout occurred. Retransmitting...")

with open(filename) as file:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for line in file:
        message = line.encode()
        send_with_timeout(client_socket, message, (dns, 6789))
    
    # Send termination message
    send_with_timeout(client_socket, b"END", (dns, 6789))
    client_socket.close()
