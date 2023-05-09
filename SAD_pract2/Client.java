import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Client {
    static BufferedReader in;
    public static void main(String[] args) {
        MySocket sc = new MySocket("localhost",2345);
        in = new BufferedReader(new InputStreamReader(System.in));
        sc.write_line(args[0]);
    
        new Thread() {
            public void run(){
                String linia;
                        try {
                            while((linia = in.readLine())!= null){
                                sc.write_line(linia);
                            
                                if(linia.matches("exit")){
                                    sc.close();
                                    break;   
                                }
                            }
                            sc.write_line("exit");
                            sc.close();
                        } catch (IOException e) {
                            // TODO Auto-generated catch block
                            e.printStackTrace();
                        }
                    
            }
        }.start();


        new Thread() {
            public void run(){
                String linia;
                    while((linia = sc.read_line()) != null){
                        if(linia.matches("exit")){
                            break;
                        }
                        System.out.println(linia);
                    }
                }
            

        }.start();
    
        
    }
}

