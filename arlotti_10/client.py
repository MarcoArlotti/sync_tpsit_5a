import socket


class Client:
    def __init__(self, host:str, porta:int):
        self.host = host
        self.porta = porta
        self.client_socket = None

    def connetti(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #crea
        self.client_socket.bind((self.host, self.porta)) #associa

    def manda(self):
        if self.client_socket:
            vai = True
            while vai:
                messaggio = str(input("scrivi il messaggio da inviare..."))
                self.client_socket.sendall(messaggio.encode("utf-8")) #manda
                risposta = str(input("continuare? y|n"))
                if risposta == "y":
                    vai = True
                if risposta == "n":
                    vai = False
                else:
                    print("ERRORE SCRIVI y|n")
        else:
            print("ERRORE connettiti ad un socket con connetti()")

    def chiudi(self):
        self.client_socket.close()
        print("SERVER CHIUSO")

client1 = Client("127.0.0.1", 8000)
client1.connetti()
client1.manda()
client1.chiudi()