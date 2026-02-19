import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.Socket;
import java.util.Scanner;

public class Client { // stesso nome del file
    public static void main(String[] args) {
        Socket socket;
        InputStreamReader inputStreamReader;
        OutputStreamWriter outputStreamWriter;
        BufferedReader bufferedReader;
        BufferedWriter bufferedWriter;
        try {
            socket = new Socket("localhost",2069); // assegnazione ip + porta

            inputStreamReader = new InputStreamReader(socket.getInputStream());
            outputStreamWriter = new OutputStreamWriter(socket.getOutputStream());

            bufferedReader = new BufferedReader(inputStreamReader);
            bufferedWriter = new BufferedWriter(outputStreamWriter);

            Scanner scanner = new Scanner(System.in); //prende la scritta dal terminale

            while (true) {
                String messaggio_da_inviare = scanner.nextLine();
                bufferedWriter.write(messaggio_da_inviare);
                bufferedWriter.newLine();
                bufferedWriter.flush();

                System.out.println("Server:" + bufferedReader.readLine());

                if (messaggio_da_inviare.equalsIgnoreCase("exit")) //se uscito esci dal while
                    break;
            }

        } catch (IOException e) {
            e.printStackTrace();
        }

    }
}