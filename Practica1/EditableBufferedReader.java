
import java.io.*;




class EditableBufferedReader extends BufferedReader {
    
    private boolean key;
    public final Line ret;
    public final Console console;

    public EditableBufferedReader(Reader in) {
        super(in);
        this.key = false;
        this.ret = new Line();
        this.console = new Console(ret);
        this.ret.addObserver(console);

    }

    public void setRaw(){
        String[] cmd = {"/bin/sh", "-c", "stty raw -echo </dev/tty"};
        try {
			Runtime.getRuntime().exec(cmd).waitFor();
		} catch (InterruptedException e) {

			e.printStackTrace();
		} catch (IOException e) {
	
			e.printStackTrace();
		}
        
    }

    public void unsetRaw() {
        String[] cmd = {"/bin/sh", "-c", "stty cooked echo </dev/tty"};
        try {
			Runtime.getRuntime().exec(cmd).waitFor();
		} catch (InterruptedException e) {

			e.printStackTrace();
		} catch (IOException e) {
	
			e.printStackTrace();
		}

    }
    @Override
    public int read() {
        int character;
        this.key = false;
        int ret;

        try{
            character = super.read();
            if(character == 27){
                this.key=true;
                character = super.read();
                character = super.read();
                if(character == 50 || character ==51){
                    super.read();
                }
            }else if(character==127){

                this.key=true;
            }
            ret = character;
            
        } catch(IOException ex){
            System.out.println("Error: "+ex);
            ret = 0;
        }

        return ret;
    }

    /* (non-Javadoc)
     * @see java.io.BufferedReader#readLine()
     */
    @Override
    public String readLine() throws IOException{
        
        char c = '\0'; 
        int number;

        setRaw();
        System.out.print("\033[4h");
        do{
            if(c==Constants.EXIT){
                unsetRaw();
                System.exit(1);
            }
            number = this.read();
            if(this.key==true){
                switch(number){
                    case Constants.RIGHT_ARROW:
                        ret.moveR(); 
                        System.out.print("\033[1C"); 
                        break;
                    case Constants.LEFT_ARROW:                      
                        ret.moveL();
                        System.out.print("\033[1D");
                          break;
                    case Constants.INI_BUTTON:
                        System.out.print("\033["+ret.gotoINI()+"D");                        
                         break;
                    case Constants.FIN_BUTTON:
                        System.out.print("\033["+ret.gotoFIN()+"C");
                         break;
                    case Constants.INS_BUTTON:
                        int mode_i = ret.modeINS();
                        if(mode_i== 1){
                            System.out.print("\033[4l");
                        }else if(mode_i == 2){
                            System.out.print("\033[4h");
                        }
               
                         break;
                    case Constants.SUPR_BUTTON:  
                        boolean mode = ret.supr();      
                        if(mode) System.out.print("\033[P");
                        break;
                    case Constants.DEL_BUTTON:
                        boolean mode_d = ret.dele();
                        if(mode_d){
                            System.out.print("\033[1D");
                            System.out.print("\033[P");   
                        }
                        break;
                }
                
            }
            else if(number!=13){
               c = (char) number; 
               ret.insert(c);
               
               
               System.out.print(c);
            }   
            
        }while(number!=13);
        unsetRaw();
        return ret.toString();
    }


}

