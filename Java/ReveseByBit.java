import java.io.PrintWriter;


public class ReveseByBit {

	private static int reveseByBit(int input){
		int res=0;
		for(int i=0;i<32;i++){
			res<<=1;
			res|=(input&1);
			input>>=1;
		}
		return res;
	}
	private static void printByBit(int input){
		String res="";
		for(int i=0;i<32;i++){
			if((input&1)==1)
				res=1+res;
			else {
				res=0+res;
			}
			input>>=1;
		}
		System.out.println(res);
	}
		
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int test=1234;
		printByBit(test);
		printByBit(reveseByBit(test));
		
	}
}
