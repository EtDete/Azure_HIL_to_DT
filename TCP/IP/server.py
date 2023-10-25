import threading
import socket

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
 
host = get_ip()
port = int(input("Chose a port >>> "))
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
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()
        
if __name__ == "__main__":
    receive()