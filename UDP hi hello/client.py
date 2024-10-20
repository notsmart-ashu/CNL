import socket
import threading

def receive_messages(sock):
    while True:
        data, addr = sock.recvfrom(1024)
        print(f"Received message from {addr}: {data.decode()}")
        if data.decode().lower() == 'exit':
            print("Server disconnected.")
            break

def send_messages(sock, server_ip, server_port):
    while True:
        message = input("Enter message to send (or type 'exit' to quit): ")
        sock.sendto(message.encode(), (server_ip, server_port))
        if message.lower() == 'exit':
            print("Client exiting...")
            break

def udp_client(server_ip="127.0.0.1", server_port=12345):
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Send initial message to connect to the server
    sock.sendto(b"Hello, Server!", (server_ip, server_port))

    # Start threads for sending and receiving messages
    receive_thread = threading.Thread(target=receive_messages, args=(sock,))
    send_thread = threading.Thread(target=send_messages, args=(sock, server_ip, server_port))
    receive_thread.start()
    send_thread.start()

    # Wait for threads to finish
    receive_thread.join()
    send_thread.join()

    sock.close()

if __name__ == "__main__":
    udp_client()
