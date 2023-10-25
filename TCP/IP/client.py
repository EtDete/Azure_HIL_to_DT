import threading
import socket
import os
import parameter as p
from time import sleep
# import parameter as p
# alias = input('Choose an alias >>> ')
host = p.Ip_cartes[0]
port = p.Port_cartes[0]
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
clients = []

def broadcast(message,client_sent):
    for things in clients:
        if client_sent !=things:
            things.send(message)
        

# Function to handle clients'connections
def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message,client_sent=client)
        except:
            # index = clients.index(client)
            clients.remove(client)
            client.close()
            break
# Main function to receive the clients connection
def receive():
    while True:
        print('Server is running and listening ...')
        client, address = server.accept()
        print(f'connection is established with {str(address)}')
        clients.append(client)
        client.send('you are now connected!'.encode('utf-8'))
        # thread = threading.Thread(target=handle_client, args=(client,))
        # thread.start()
    
    
def create_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Ip_address = get_ip()
    client.connect((Ip_address, 55000))
    return client
    
    
def get_ip():
     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
     s.settimeout(0)
     try:
         s.connect(('10.254.254.254', 1))
         IP = s.getsockname()[0]
     except Exception:
         IP = "127.0.0.1"
     finally:
         s.close()
     return IP

def client_receive(client):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            print(message)
        except:
            print('Error!')
            client.close()
            break


def client_send(client):
    while True:
        message = input("")
        client.send(message.encode('utf-8'))

# receive_thread = threading.Thread(target=client_receive)
# receive_thread.start()

# send_thread = threading.Thread(target=client_send)
# send_thread.start()
if __name__ == "__main__":
    client = create_client()
    thread = threading.Thread(target=receive, args=())
    thread.start()

    receive_thread = threading.Thread(target=client_receive, args=(client,))
    receive_thread.start()

    send_thread = threading.Thread(target=client_send, args=(client,))
    send_thread.start()
    receive_thread = threading.Thread(target=client_receive, args=(client,))
    receive_thread.start()