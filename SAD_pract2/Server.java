import java.util.HashMap;
import java.util.Map;
//SocketServer associat a cada Client diferent
public class Server {
    
    public static void main(String[] args) {
    MyServerSocket sc = new MyServerSocket(2345);
    Map <String,MySocket> diccionari = new HashMap<String,MySocket>();
    

    while(true){
        MySocket socket= sc.accept();
        System.out.println("Connected");
        
        new Thread() {
            public void run(){
                String nickname = socket.read_line();
                diccionari.put(nickname, socket);
                System.out.println("Welcome " + nickname);
                String linia;
                while((linia = socket.read_line()) != null){
                    
                    if(linia.matches("exit")){
                            System.out.println("ha sortit " + nickname);
                            linia= "ha sortit del chat" ;        
                            diccionari.remove(nickname);

                        }
                    for (String nicknames : diccionari.keySet()){
                        //envies missatge al client 
                        

                        if(nicknames!=nickname){
                            diccionari.get(nicknames).write_line(nickname+": "+linia);
                        }
                    }
                }

                socket.close();

            }
        }.start();

    
    }
    }
}
