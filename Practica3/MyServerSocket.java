import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.HashMap;
import java.util.Map;

public class MyServerSocket{

    ServerSocket socket;

    public MyServerSocket(int port){
        try {
            this.socket = new ServerSocket(port);
        } catch (Exception e) {
            // TODO: handle exception
        }

    }

    public MySocket accept(){

        try {
            return new MySocket(socket.accept());
        } catch (Exception e) {
            // TODO: handle exception
        }
        return null;
    }
    
}