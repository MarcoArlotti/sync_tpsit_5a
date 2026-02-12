### Spiegazione riga per riga del client Java

Di seguito trovi il codice originale seguito da una spiegazione dettagliata, riga per riga. Ogni blocco spiega **cosa fa** la riga o il gruppo di righe e **perché** è scritto così.

```java
import java.io.*;
import java.net.*;
```
1. **`import java.io.*;`**  
   **Cosa fa:** importa tutte le classi del pacchetto `java.io` (es. `DataInputStream`, `DataOutputStream`, `BufferedReader`, `InputStreamReader`).  
   **Perché:** servono per leggere/scrivere dati e per leggere dalla console.   [docs.oracle.com](https://docs.oracle.com/javase/tutorial/essential/io/datastreams.html)

2. **`import java.net.*;`**  
   **Cosa fa:** importa tutte le classi del pacchetto `java.net` (es. `Socket`).  
   **Perché:** `Socket` è la classe che rappresenta una connessione TCP verso un host/porta.   [GeeksForGeeks](https://www.geeksforgeeks.org/java/socket-programming-in-java/)

---

```java
public class SimpleClient {
```
3. **Dichiarazione della classe**  
   **Cosa fa:** definisce una classe pubblica chiamata `SimpleClient`. In Java il `main` deve essere contenuto in una classe.  

---

```java
    public static void main(String[] args) {
```
4. **Metodo main**  
   **Cosa fa:** punto di ingresso dell'applicazione. `public static void main(String[] args)` è la firma standard che la JVM cerca per avviare il programma.

---

```java
        String host = "localhost";
        int porta = 69420;
```
5. **Variabili di configurazione**  
   **`host`**: nome o indirizzo IP del server a cui connettersi. Qui `localhost` indica la stessa macchina.  
   **`porta`**: porta TCP su cui il server è in ascolto. Devono corrispondere ai valori usati dal server.   [GeeksForGeeks](https://www.geeksforgeeks.org/java/socket-programming-in-java/)

---

```java
        try (Socket socket = new Socket(host, porta);
             DataOutputStream out = new DataOutputStream(socket.getOutputStream());
             DataInputStream in = new DataInputStream(socket.getInputStream());
             BufferedReader console = new BufferedReader(new InputStreamReader(System.in))) {
```
6. **Try-with-resources e creazione delle risorse**  
   **`try (...) {`**: apre un blocco try-with-resources che chiude automaticamente tutte le risorse dichiarate alla fine del blocco, anche in caso di eccezione. Questo evita leak di risorse.   [Baeldung](https://www.baeldung.com/java-inputstream-server-socket)

   - **`new Socket(host, porta)`**  
     **Cosa fa:** apre una connessione TCP verso `host:porta`. Se la connessione fallisce viene lanciata un`IOException`.   [GeeksForGeeks](https://www.geeksforgeeks.org/java/socket-programming-in-java/)

   - **`new DataOutputStream(socket.getOutputStream())`**  
     **Cosa fa:** avvolge lo stream di output del socket in un `DataOutputStream`, che fornisce metodi per scrivere tipi primitivi e stringhe in formato binario (es. `writeUTF`).   [docs.oracle.com](https://docs.oracle.com/javase/tutorial/essential/io/datastreams.html)

   - **`new DataInputStream(socket.getInputStream())`**  
     **Cosa fa:** avvolge lo stream di input del socket in un `DataInputStream`, che permette di leggere dati con metodi come `readUTF`. Devono corrispondere i formati di scrittura/lettura tra client e server.   [docs.oracle.com](https://docs.oracle.com/javase/tutorial/essential/io/datastreams.html)

   - **`new BufferedReader(new InputStreamReader(System.in))`**  
     **Cosa fa:** crea un lettore per la console; `InputStreamReader(System.in)` converte byte in caratteri, `BufferedReader` aggiunge buffering e `readLine()` comodo per leggere una riga.   [docs.oracle.com](https://docs.oracle.com/javase/tutorial/essential/io/datastreams.html)

---

```java
            System.out.println("Connesso al server " + host + ":" + porta);
            System.out.print("Inserisci il messaggio da inviare: ");
            String messaggio = console.readLine();
```
7. **Interazione con l'utente**  
   - **`System.out.println(...)`**: stampa conferma di connessione.  
   - **`System.out.print(...)`**: stampa il prompt senza andare a capo.  
   - **`console.readLine()`**: legge una riga inserita dall'utente nella console e la assegna a `messaggio`. Se l'utente preme solo Enter, `messaggio` sarà una stringa vuota; se la console è chiusa, può lanciare `IOException`.   [docs.oracle.com](https://docs.oracle.com/javase/tutorial/essential/io/datastreams.html)

---

```java
            out.writeUTF(messaggio);
            out.flush();
```
8. **Invio del messaggio al server**  
   - **`out.writeUTF(messaggio)`**: scrive la stringa in formato UTF-8 preceduta dalla sua lunghezza (formato usato da `DataOutputStream`/`DataInputStream`). Il server deve usare `readUTF()` per leggere correttamente.   [docs.oracle.com](https://docs.oracle.com/javase/tutorial/essential/io/datastreams.html)  
   - **`out.flush()`**: forza l'invio immediato dei dati sullo stream; utile per assicurarsi che il messaggio non resti in un buffer locale.

---

```java
            String risposta = in.readUTF();
            System.out.println("Risposta dal server: " + risposta);
```
9. **Ricezione della risposta**  
   - **`in.readUTF()`**: legge una stringa inviata dal server con `writeUTF`. Questo metodo è bloccante: il thread aspetta finché non arriva la stringa o si verifica un errore/chiusura della connessione.   [docs.oracle.com](https://docs.oracle.com/javase/tutorial/essential/io/datastreams.html)  
   - **`System.out.println(...)`**: stampa la risposta ricevuta.

---

```java
        } catch (IOException e) {
            System.err.println("Errore di I/O: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
```
10. **Gestione delle eccezioni e chiusura**  
    - **`catch (IOException e)`**: intercetta errori di rete o I/O (es. server non raggiungibile, stream chiuso).  
    - **`System.err.println(...)`**: stampa un messaggio di errore su `stderr`.  
    - **`e.printStackTrace()`**: stampa lo stack trace per debug.  
    - **Chiusura risorse:** grazie al try-with-resources tutte le risorse (`socket`, `in`, `out`, `console`) vengono chiuse automaticamente al termine del blocco, anche in caso di eccezione.   [Baeldung](https://www.baeldung.com/java-inputstream-server-socket)  [docs.oracle.com](https://docs.oracle.com/javase/tutorial/essential/io/datastreams.html)

---

### Note pratiche e suggerimenti
- **Compatibilità formato**: assicurati che il server usi `DataInputStream.readUTF()` per leggere e `DataOutputStream.writeUTF()` per rispondere; altrimenti i metodi non saranno compatibili.   [docs.oracle.com](https://docs.oracle.com/javase/tutorial/essential/io/datastreams.html)  
- **Connessioni multiple**: questo client apre una connessione, invia un messaggio e poi termina. Per inviare più messaggi senza riconnettersi, metti l'invio/lettura dentro un ciclo e prevedi una condizione di uscita (es. messaggio `"exit"`).   [GeeksForGeeks](https://www.geeksforgeeks.org/java/socket-programming-in-java/)  
- **Timeout**: puoi impostare timeout sul socket con `socket.setSoTimeout(ms)` per evitare blocchi indefiniti su `readUTF()`.   [GeeksForGeeks](https://www.geeksforgeeks.org/java/socket-programming-in-java/)

---

Se vuoi, posso:
- mostrare una versione che invia più messaggi in loop;  
- aggiungere gestione dei timeout;  
- fornire un esempio di server che gestisce più client con thread.