import socket

class Client:
    def __init__(self, host:str, porta:int):
        self.host = host
        self.porta = porta
        self.client_socket = None
    
    def connetti(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #crea
        self.client_socket.connect((self.host, self.porta)) #connettiti
        print("RICEVUTO DAL SERVER: ", self.client_socket.recv(1024).decode()) #ricevi

        messaggio = input("INVIA MESSAGGIO AL SERVER: ")
        self.client_socket.send(messaggio.encode()) #manda

        self.client_socket.close()
        print("CLIENT CHIUSO")

client1 = Client("127.0.0.1", 5000)
client1.connetti()