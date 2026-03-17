import socket
import threading

class Server:
    def __init__(self, host: str, porta: int):
        self.host = host
        self.porta = porta
        self.server_socket = None
        self.client = []
        self.nicknames = []

    def avvia(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.porta))
        self.server_socket.listen(5)
        print("SERVER IN ASCOLTO...")

    def broadcast(self, messaggio):
        print(f"[BROADCAST] Messaggio inviato a tutti: {messaggio.decode()}")  # Log messaggio broadcast
        for c in self.client:
            try:
                c.send(messaggio)
            except:
                # Se il client è disconnesso, rimuovilo dalla lista
                self.client.remove(c)

    def gestisci_client(self, client):
        while True:
            try:
                messaggio = client.recv(1024)  # Ricevi messaggio dal client
                if not messaggio:  # Se il messaggio è vuoto, significa che il client si è disconnesso
                    break
                print(f"[MESSAGGIO RICEVUTO]: {messaggio.decode()}")  # Log messaggio ricevuto
                self.broadcast(messaggio)
            except Exception as e:
                print(f"Errore nella ricezione del messaggio: {e}")
                break

        # Gestisci la disconnessione del client
        nickname = self.nicknames[self.client.index(client)]
        self.client.remove(client)
        self.nicknames.remove(nickname)
        print(f"{nickname} disconnesso")
        self.broadcast(f"{nickname} è uscito dalla chat".encode())
        client.close()

    def ricevi(self):
        while True:
            try:
                client, address = self.server_socket.accept()
                print(f"Connesso con {address}")

                client.send("NICK".encode())  # Richiedi il nickname al client
                nickname = client.recv(1024).decode()  # Ricevi il nickname

                if nickname:  # Verifica se il client ha inviato un nickname valido
                    self.nicknames.append(nickname)
                    self.client.append(client)
                    print(f"Nickname: {nickname}")

                    self.broadcast(f"{nickname} è entrato nella chat!".encode())
                    client.send("Connesso al server!".encode())  # Risposta di benvenuto al client

                    # Avvia il thread per gestire la comunicazione con il client
                    thread = threading.Thread(target=self.gestisci_client, args=(client,))
                    thread.daemon = True
                    thread.start()

            except Exception as e:
                print(f"Errore durante la connessione: {e}")

# Avvio del server
server = Server("127.0.0.1", 5002)
server.avvia()
server.ricevi()