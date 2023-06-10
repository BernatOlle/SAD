import java.util.HashMap;
import java.util.Map;

//SocketServer associat a cada Client diferent
public class Server {

    public static void main(String[] args) {
        MyServerSocket sc = new MyServerSocket(2345);
        Map<String, MySocket> diccionari = new HashMap<String, MySocket>();

        while (true) {
            MySocket socket = sc.accept();

            new Thread() {
                public void run() {
                    String nickname = socket.read_line();
                    

                    while (diccionari.containsKey(nickname)) {
                        socket.write_line("Exist");
                        nickname = socket.read_line();
                    } 

                        socket.write_line("No_Exist");
                        System.out.println(nickname+" connectat/da al servidor");
                        diccionari.put(nickname, socket);
                        String message = "?%" + nickname;

                        for (String nicknames : diccionari.keySet()) {
                            if (nicknames != nickname) {
                                diccionari.get(nicknames).write_line(message);
                            }
                        }
                        String linia;
                        while ((linia = socket.read_line()) != null) {

                            if (linia.contains("Exit?%")) {
                                String username = linia.substring(6);
                                System.out.println("Ha sortit " + username);
                                linia = "Exit?%" + username;
                                diccionari.remove(username);

                            }
                            for (String nicknames : diccionari.keySet()) {
                                // envies missatge al client

                                if (nicknames != nickname) {
                                    if (linia.contains("?%")) {
                                        System.out.println(linia);
                                        diccionari.get(nicknames).write_line(linia);
                                    } else {
                                        System.out.println(linia);
                                        diccionari.get(nicknames).write_line(nickname + ": " + linia);
                                    }
                                
                            }
                        }
                    }

                    socket.close();

                }
            }.start();

        }
    }
}
