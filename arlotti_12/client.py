import socket
import threading

class Client:
    def __init__(self, host: str, porta: int):
        self.host = host
        self.porta = porta
        self.client_socket = None
        self.nickname = input("Scegli nickname: ")

    def ricevi(self):
        while True:
            try:
                messaggio = self.client_socket.recv(1024).decode()
                if messaggio == "NICK":
                    self.client_socket.send(self.nickname.encode())
                else:
                    print("\n" + messaggio)
            except:
                print("Connessione chiusa")
                self.client_socket.close()
                break

    def scrivi(self):
        while True:
            msg = input("INVIA MESSAGGIO AL SERVER: ")  # Messaggio di prompt
            try:
                self.client_socket.send(f"{self.nickname}: {msg}".encode())  # Invia al server
            except:
                break

    def connetti(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.porta))

        print("Connesso al server!")

        # Thread per ricevere
        threading.Thread(target=self.ricevi, daemon=True).start()

        # Thread per scrivere
        threading.Thread(target=self.scrivi, daemon=True).start()

        while True:
            pass  # Mantieni il client attivo in attesa di input

client1 = Client("127.0.0.1", 5002)
client1.connetti()