import socket
import threading

def receive_messages(sock):
    while True:
        data, addr = sock.recvfrom(1024)
        print(f"Received message from {addr}: {data.decode()}")
        if data.decode().lower() == 'exit':
            print("Client disconnected.")
            break

def send_messages(sock, client_addr):
    while True:
        message = input("Enter message to send (or type 'exit' to quit): ")
        sock.sendto(message.encode(), client_addr)
        if message.lower() == 'exit':
            print("Server exiting...")
            break

def udp_server(host="0.0.0.0", port=12345):
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))
    print(f"UDP Server listening on {host}:{port}...")

    data, client_addr = sock.recvfrom(1024)
    print(f"Connected to client at {client_addr}")

    # Start threads for sending and receiving messages
    receive_thread = threading.Thread(target=receive_messages, args=(sock,))
    send_thread = threading.Thread(target=send_messages, args=(sock, client_addr))
    receive_thread.start()
    send_thread.start()

    # Wait for threads to finish
    receive_thread.join()
    send_thread.join()

    sock.close()

if __name__ == "__main__":
    udp_server()
