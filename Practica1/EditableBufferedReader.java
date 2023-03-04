
import java.io.*;




class EditableBufferedReader extends BufferedReader {
    
    private boolean key;
    Line ret= new Line();

    public EditableBufferedReader(Reader in) {
        super(in);
        this.key = false;

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
                        break;
                    case Constants.LEFT_ARROW:
                        ret.moveL();
                          break;
                    case Constants.INI_BUTTON:
                        ret.gotoINI();                        
                         break;
                    case Constants.FIN_BUTTON:
                    
                        ret.gotoFIN();  
                         break;
                    case Constants.INS_BUTTON:
                        ret.modeINS();
                         break;
                    case Constants.SUPR_BUTTON:  
                        ret.supr();        
                        break;
                    case Constants.DEL_BUTTON:
                        ret.dele();
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

