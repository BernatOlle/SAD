import java.io.*;


class EditableBufferedReader extends BufferedReader {
    
    private boolean key;

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
        String[] cmd = {"/bin/sh", "-c", "stty cooked -echo </dev/tty"};
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
            System.out.println(character);

            if(character == 27){
                this.key=true;
                character = super.read();
                System.out.println(character);
                character = super.read();
                System.out.println(character);
                if(character == 50 && character ==51){
                    super.read();
                }
                
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
        String ret= new String();
        char c = '\0';
        //setRaw();

        while(c!='\n'){
            c = (char) read();
            if(this.key==true){
                switch(c){
                    case Constants.RIGHT_ARROW:
                                                break;
                    case Constants.LEFT_ARROW:
                                                break;
                    case Constants.INI_BUTTON:
                                                break;
                    case Constants.FIN_BUTTON:
                                                break;
                    case Constants.INS_BUTTON:
                                                break;
                    case Constants.DEL_BUTTON:
                                                break;
                }
            }
            else{
                ret+=c;
            }
            
        }
        //unsetRaw();

        return ret;

    }


}
