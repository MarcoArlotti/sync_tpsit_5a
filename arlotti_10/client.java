import java.io *;
import java.net *;

public class SimpleClient {
    public static void main(String[] args) {
        String host = "localhost";
        int porta = 69420;

        try (Socket socket = new Socket(host, porta);
            DataOutputStream out = new.DataOutputStream(socket.getOutputStream());
            DataInputStream in = new.DataInputStream(socket.getInputStream());
            BufferedReader console = new BufferedReader(new InputStreamReader(System.in))) {
                System.out.println("connesso al server" + host + ":" + porta);
                System.out.print("inserisci il messaggio da inviare: ");
                String messaggio = console.readline();

                out.writeUTF(messaggio);
                out.flush();

                String risposta = in.readUTF();
                System.out.println("risposta dal server:" + risposta);
                
            }
            
    }
}