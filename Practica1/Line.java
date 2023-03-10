import java.util.Observable;

public class Line extends Observable {

    public static final int BUFFER_CAPACITY = 16;
    private StringBuffer buff;
    private int cursor;
    private boolean modo_ins;

    public Line(){
        this.buff= new StringBuffer(BUFFER_CAPACITY);
        this.cursor=0;
        this.modo_ins = false;
    }

    public int buff_length(){
        return buff.length();
    }

   
    public void moveR(){    

        int posicio=this.cursor+1;
         if(posicio<=this.buff.length()){
            notifyObservers(Constants.RIGHT_ARROW);
            this.cursor+=1;
         }
    }
     
    public void moveL(){

        if(this.cursor!=0){
            notifyObservers(Constants.LEFT_ARROW);
            this.cursor-=1;
        }

    }
    
    public int gotoINI(){
        int cur_cursor = this.cursor;
        this.cursor=0;
        return cur_cursor;
    }

    public int gotoFIN(){
        int cur_cursor = this.buff_length() - this.cursor;
        this.cursor = this.buff.length();
        return cur_cursor;
    }

    public boolean dele(){
        boolean mode_d = false;
        if(this.cursor!=0){
            buff.deleteCharAt(this.cursor-1);
            
            this.cursor-=1;
            mode_d = true;
        }
        return mode_d;
    }

    public boolean supr(){
        boolean mode = false;
        if(this.cursor<this.buff.length()){
            buff.deleteCharAt(this.cursor);   
            mode = true;
        }
        return mode;
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
    public int modeINS(){
        modo_ins = !modo_ins;
        int mode_i = 1;
        /*   
        if(!modo_ins){
            mode_i = 1;
            modo_ins=true;
        }else{
            mode_i = 2;
            modo_ins=false;
        }
        */
        return mode_i;
    }
    public void insert(char c){
        if(this.cursor==this.buff.capacity()){
            StringBuffer buff2 = new StringBuffer(BUFFER_CAPACITY);
           buff.append(buff2);
       }
        if(modo_ins && this.cursor  < this.buff_length()){          
            buff.setCharAt(this.cursor, c);
            this.cursor+=1;
            
        }else{
            if(this.cursor  < this.buff_length()){

            }
            buff.insert(this.cursor, c);
            this.cursor+=1;
        }

        
    }



    public String toString(){
        return this.buff.toString();
    }
       
}
