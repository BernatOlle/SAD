class Line {

    public static final int BUFFER_CAPACITY = 16;
    private StringBuffer buff;
    private int cursor;
    private boolean modo_ins=false;

    public Line(){
        this.buff= new StringBuffer(BUFFER_CAPACITY);
        this.cursor=0;
    }

    public int buff_length(){
        return buff.length();
    }

   
    public void moveR(){    

        int posicio=this.cursor+1;
         if(posicio<=this.buff.length()){
            System.out.print("\033[1C");
            this.cursor+=1;
         }
    }
     
    public void moveL(){

        if(this.cursor!=0){
            System.out.print("\033[1D");
            this.cursor-=1;
        }

    }
    
    public void gotoINI(){
        System.out.print("\033["+cursor+"D");
        this.cursor=0;
    }

    public void gotoFIN(){
        System.out.print("\033["+(this.buff_length()-this.cursor)+"C");
        this.cursor=this.buff.length();
    }

    public void dele(){
        if(this.cursor!=0){
            buff.deleteCharAt(this.cursor-1);
            System.out.print("\033[1D");
            System.out.print("\033[P");
            this.cursor-=1;
        }
    }

    public void supr(){
        if(this.cursor<this.buff.length()){
            buff.deleteCharAt(this.cursor);
            System.out.print("\033[P");
            
        }
    }

     /*
    public void insert(char c){
       if(this.cursor==this.buff.capacity()){
            StringBuffer buff2 = new StringBuffer(BUFFER_CAPACITY);
            buff.append(buff2);
       }
        buff.insert(this.cursor, c);
        this.cursor+=1;
    }*/
    public void modeINS(){
        if(modo_ins==false){
            modo_ins=true;
        }else{
            modo_ins=false;
        }
    }
    public void insert(char c){
        if(this.cursor==this.buff.capacity()){
            StringBuffer buff2 = new StringBuffer(BUFFER_CAPACITY);
           buff.append(buff2);
       }
        if(modo_ins && this.cursor  < this.buff_length()){
            System.out.print("\033[4l");
            buff.setCharAt(this.cursor, c);
            this.cursor+=1;
        }else{
            if(this.cursor  < this.buff_length()){
                
                System.out.print("\033[4h");
            }
            buff.insert(this.cursor, c);
            this.cursor+=1;
        }
    }



    public String toString(){
        return this.buff.toString();
    }
       
}
