import threading
import socket




class Client:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((str(input("Quelle l'IP du serveur ? >>> ")), 55000))

        self.receive_thread = threading.Thread(target=self.client_receive)
        self.receive_thread.start()

        self.send_thread = threading.Thread(target=self.client_send)
        self.send_thread.start()

    def __enter__(self):
        self.__init__()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.client.close()

    def client_receive(self):
        while True:
            try:
                message = self.client.recv(1024).decode('utf-8')
                print(message)
            except Exception as e:
                print('Error !', e)
                self.client.close()
                break

    def client_send(self):
        while True:
            message = input(">>>  ")
            self.client.send(message.encode('utf-8'))

