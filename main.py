import socket 
import threading


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server_socket.bind(("localhost", 12345))
server_socket.listen()


clients = []

def broadcast(message, sender_socket): 
    for client in clients:
        if client != sender_socket: 
            client.send(message)

def handle_client(client_socket): 
    while True: 
        try: 
            message = client_socket.recv(1024)
            if message:
                print(f"Recieved {message.decode()}")
                broadcast(message, client_socket)


            else: 
                remove_client(client_socket)            
        except:
            remove_client(client_socket)
            break
def remove_client(client_socket):
    if client_socket in clients: 
        clients.remove(client_socket)
        client_socket.close() 

def start_server(): 
    print("Server started on port 12345")
    while True: 
        client_socket, addr = server_socket.accept()
        print(f"Connected to {addr}")   
        clients.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()



if __name__ == "__main__":
    start_server()



