### Spiegazione riga per riga

Di seguito riporto il codice originale con **ogni riga** seguita da una spiegazione chiara e concisa in italiano.

```java
import java.io.*;
```
- **Importa le classi di I/O** necessarie (stream, eccezioni, ecc.).  
- Serve per usare `DataInputStream`, `DataOutputStream`, `IOException` e altre classi di input/output.

```java
import java.net.*;
```
- **Importa le classi di rete** (Socket, ServerSocket, InetAddress, ecc.).  
- Necessario per creare server e client TCP.

```java
public class Server {
```
- **Dichiarazione della classe pubblica** chiamata `Server`.  
- Il file deve chiamarsi `Server.java` perché la classe è pubblica.

```java
    public static void main(String[] args) {
```
- **Metodo `main`**, punto di ingresso dell'applicazione Java.  
- `public` = accessibile; `static` = eseguibile senza istanziare la classe; `String[] args` = argomenti da linea di comando.

```java
        int porta = 5000;
```
- **Definisce la porta TCP** su cui il server ascolterà le connessioni in ingresso.  
- Le porte sotto 1024 richiedono permessi di sistema; 5000 è una porta arbitraria non privilegiata.

```java
        try (ServerSocket serverSocket = new ServerSocket(porta)) {
```
- **Crea un `ServerSocket` legato alla porta 5000** usando il costruttore.  
- La sintassi `try (...) {` è il **try-with-resources**: chiude automaticamente `serverSocket` alla fine del blocco.  
- Se la porta è già in uso o non disponibile viene lanciata un'eccezione `IOException`.   [GeeksForGeeks](https://www.geeksforgeeks.org/java/java-net-serversocket-class-in-java/)

```java
            System.out.println("Server in ascolto sulla porta " + porta);
```
- **Stampa un messaggio sulla console** per indicare che il server è pronto ad accettare connessioni.

```java
            Socket socket = serverSocket.accept();
```
- **Blocca e attende una connessione in ingresso**; quando un client si connette, `accept()` restituisce un oggetto `Socket` che rappresenta la connessione punto‑a‑punto.  
- `accept()` è bloccante: il programma resta qui finché non arriva un client.   [GeeksForGeeks](https://www.geeksforgeeks.org/java/java-net-serversocket-class-in-java/)

```java
            System.out.println("Client connesso!");
```
- **Stampa che un client si è connesso**; utile per debug e log.

```java
            DataInputStream in = new DataInputStream(socket.getInputStream());
```
- **Crea un `DataInputStream`** avvolgendo lo stream di input del socket.  
- `DataInputStream` fornisce metodi per leggere tipi primitivi e stringhe in formato binario (es. `readUTF()`).   [Stack Overflow](https://stackoverflow.com/questions/4009157/java-socket-writeutf-and-readutf)  [codingtechroom.com](https://codingtechroom.com/question/understanding-java-socket-communication-the-use-of-writeutf-and-readutf-methods)

```java
            DataOutputStream out = new DataOutputStream(socket.getOutputStream());
```
- **Crea un `DataOutputStream`** avvolgendo lo stream di output del socket.  
- Permette di scrivere tipi primitivi e stringhe con `writeUTF()` che il client può leggere con `readUTF()`.   [Stack Overflow](https://stackoverflow.com/questions/4009157/java-socket-writeutf-and-readutf)

```java
            String msg = in.readUTF();
```
- **Legge una stringa inviata dal client** usando il formato `modified UTF-8` previsto da `readUTF()`.  
- `readUTF()` legge prima la lunghezza e poi i byte della stringa, quindi è sincronizzato con `writeUTF()` lato client.   [Stack Overflow](https://stackoverflow.com/questions/4009157/java-socket-writeutf-and-readutf)

```java
            System.out.println("Messaggio ricevuto: " + msg);
```
- **Stampa il messaggio ricevuto** sulla console del server.

```java
            out.writeUTF("Ciao client, ho ricevuto il tuo messaggio!");
```
- **Invia una stringa di risposta al client** usando `writeUTF()`.  
- Il client deve usare `readUTF()` per leggere correttamente questa risposta.   [Stack Overflow](https://stackoverflow.com/questions/4009157/java-socket-writeutf-and-readutf)

```java
            socket.close();
```
- **Chiude la connessione con il client**.  
- Dopo `close()` lo stream e il socket non sono più utilizzabili. Nota: il `ServerSocket` rimane aperto finché non termina il blocco `try-with-resources`.

```java
        } catch (IOException e) {
```
- **Cattura eccezioni di I/O** che possono verificarsi durante la creazione del server, l'accettazione della connessione o la lettura/scrittura sugli stream.

```java
            e.printStackTrace();
```
- **Stampa lo stack trace dell'eccezione** sulla console; utile per debug ma non ideale in produzione (meglio loggare in modo strutturato).

```java
        }
    }
}
```
- **Chiusura dei blocchi**: termina il `catch`, il `main` e la classe `Server`.

---

### Note pratiche e miglioramenti consigliati
- **Server single‑client**: il codice accetta una sola connessione e poi termina. Per gestire più client contemporaneamente, bisogna creare un **thread** (o usare un pool di thread) per ogni `Socket` accettato.  
- **Risorse**: usare try-with-resources anche per `Socket`, `DataInputStream` e `DataOutputStream` per garantire la chiusura automatica.  
- **Protocollo**: `readUTF`/`writeUTF` è comodo per stringhe, ma per protocolli più complessi conviene definire un formato (es. JSON) e usare `BufferedReader`/`PrintWriter` o stream binari strutturati.   [Stack Overflow](https://stackoverflow.com/questions/4009157/java-socket-writeutf-and-readutf)  [codingtechroom.com](https://codingtechroom.com/question/understanding-java-socket-communication-the-use-of-writeutf-and-readutf-methods)

---

### Esempio rapido di miglioramento (concetto)
- Accettare connessioni in un ciclo `while(true)` e per ogni `accept()` avviare un nuovo `Thread` che gestisce la comunicazione con quel client. Questo rende il server **concorrenziale** e capace di servire più client contemporaneamente.

---

Se vuoi, ti mostro subito **la versione multithread completa** del server e il client corrispondente, e ti spiego come compilarli ed eseguirli passo passo.