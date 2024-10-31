import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if message:
                print(f"\n{client_socket.getsockname()[1]}: {message}\n")
            else:
                break
        except:
            print("Connection closed.")
            break

def send_messages(client_socket):
    while True:
        message = input("You: ")
        client_socket.send(message.encode())

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost", 12345))

    # Start threads for sending and receiving
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    send_thread = threading.Thread(target=send_messages, args=(client_socket,))
    receive_thread.start()
    send_thread.start()



if __name__ == "__main__":
    start_client()