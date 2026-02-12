import java.io.*;
import java.net.*;

public class SimpleServer {
    public static void main(String[] args) {
        int porta = 69420;

        try (ServerSocket serverSocket = new ServerSocket(porta);
             Socket socket = serverSocket.accept();
             DataInputStream in = new DataInputStream(socket.getInputStream());
             DataOutputStream out = new DataOutputStream(socket.getOutputStream())) {

            System.out.println("Server in ascolto sulla porta " + porta);
            System.out.println("Client connesso...");

            String messaggio = in.readUTF();
            System.out.println("Messaggio ricevuto: " + messaggio);

            out.writeUTF("Ciao client, ho ricevuto il messaggio");
        }
        catch (IOException e) {
            e.printStackTrace();
        }
    }
}
