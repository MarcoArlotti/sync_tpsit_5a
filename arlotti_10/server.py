import socket

class Server:
    def __init__(self,host:str, porta:int):
        self.host = host
        self.porta = porta
        self.server_socket = None
    
    def avvia(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #crea
        self.server_socket.bind((self.host, self.porta)) #associa
    
    def ascolta(self):
        self.server_socket.listen(5) #ascolta
        print("SERVER IN ASCOLTO...")

        client, address = self.server_socket.accept() #accetta
        print(f"CONNESSIONE DA {address}")
        client.send("we sono il server".encode()) #manda
        print("RICEVUTO DAL CLIENT: ", client.recv(1024).decode()) #ricevi

        self.server_socket.close()
        print("SERVER CHIUSO")
        
server1 = Server("127.0.0.1", 5000)
server1.avvia()
server1.ascolta()