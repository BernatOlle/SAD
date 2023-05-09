import java.util.Observer;
import java.util.Observable;


public class Console implements Observer {
	private Line line;

	public Console(Line line){
		this.line = line;
	}
        @Override
	public void update(Observable o, Object arg){
		int seq = ((Integer)arg).intValue();
		//System.out.print(seq);

		switch (seq){
			case Constants.SUPR_BUTTON:
				System.out.print("\033[1D");
				System.out.print("\033[P"); 
				break;
			case Constants.LEFT_ARROW:
				System.out.print("\033[1D");
				break;
			case Constants.RIGHT_ARROW:
				System.out.print("\033[1C"); 
				break;
			case Constants.INI_BUTTON:
				System.out.print("\033["+ret.gotoINI()+"D"); 
				break;
			case Constants.FIN_BUTTON:
				System.out.print("\033["+ret.gotoFIN()+"C");
				break;
			case Constants.DEL_BUTTON:
				System.out.print("\033[1D");
				System.out.print("\033[P");  
				break;
			case Constants.INS_BUTTON:
				int mode_i = ret.modeINS();
				if(mode_i== 1){
					System.out.print("\033[4l");
				}else if(mode_i == 2){
					System.out.print("\033[4h");
				}
				break;
		}
	}
}