import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.Socket;
import java.util.Scanner;
import java.util.stream.Stream;

public class Client { // stesso nome del file
    public static void main(String[] args) {

        Socket socket = null;
        
        InputStreamReader inputStreamReader = null;
        OutputStreamWriter outputStreamWriter = null;

        BufferedReader bufferedReader = null; //velocizza la ricezione e del messaggio
        BufferedWriter bufferedWriter = null;

        
        try {
            Socket = new Socket('localhost',69420); // assegnazione ip + porta

            inputStreamReader = new InputStreamReader(Socket.getInputStream());
            outputStreamWriter = new OutputStreamWriter(Socket.getOutputStream());

            bufferedReader = new BufferedReader(inputStreamReader);
            bufferedWriter = new BufferedWriter(outputStreamWriter);

            Scanner scanner = new Scanner(System.in); //prende la scritta dal terminale

            while (true) {
                String messaggio_da_inviare = scanner.nextLine();
                bufferedWriter.write(messaggio_da_inviare);
                bufferedWriter.newLine();
            }
        }  
    }
}