import java.net.Socket;
import java.io.*;




public class MySocket{

    public Socket socket;
    BufferedReader in;
    PrintWriter out;
    //S'ha de crear un Thread que llegeixi el Input
    //S'ha de crear un Thread que escrigui per el Output
    //S'ha de crear un Thread que detecti el que escrius per teclat
    public MySocket(String host,int port){
        try {
            socket = new Socket(host,port);
            in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            out = new PrintWriter(socket.getOutputStream(), true);
        } catch (Exception e) {
            // TODO: handle exception
        }
    }

    public MySocket(Socket so){
        try {
            socket = so;
            in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            out = new PrintWriter(socket.getOutputStream(), true);
        } catch (Exception e) {
            // TODO: handle exception
        }
    }

    public String read_line(){
        try {
            return in.readLine();
        } catch (Exception e) {
            // TODO: handle exception
        }
        return null;
    }

    public void write_line(String line){
        try {
            out.println(line);
            out.flush();
        } catch (Exception e) {
            // TODO: handle exception
        }
    }
    
    public void close(){
        try {
            socket.close();
            in.close();
            out.close();
        } catch (Exception e) {
            // TODO: handle exception
        }
    }

}