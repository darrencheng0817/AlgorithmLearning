
import java.util.HashMap;
import java.util.LinkedList;
import java.util.List;


public class test {
	static int count=0;
	public static void main(String[] args) throws Exception {
		printBrinary(5);
		printBrinary(7);
		printBrinary(5&6&7);
		System.out.println(countBits(8844000));
		System.out.println(isPowerOfTwo(-4));
		List<String> testList=new LinkedList<String>();
		System.out.println(isPow4((int)Math.pow(4, 5)));
		System.out.println(myABS(-4245));
		HashMap<Integer, Integer> map=new HashMap<Integer, Integer>();
		map.put(1, 2);
		map.put(2, 9);
		for(int i:map.keySet()){
			System.out.println(map.get(i));
		}
        int[] nums={1,2,3,4,5};
        System.out.println(canWinNim(41));
        System.out.println(count);
        System.out.println(closestPalindrome(19999));
	}
	public static long closestPalindrome(long x) {
            String mirrorString = mirrorLeft(String.valueOf(x));
            StringBuilder sb = new StringBuilder(String.valueOf(x));
            int len = sb.length();
            int idx = (len-1)/2;
            if(Long.valueOf(mirrorString)>x) {                        
                    while(idx>=0) {
                            if(sb.charAt(idx)=='0') {
                                    sb.setCharAt(idx, '9');
                                    idx--;
                            }
                            else {
                                    sb.setCharAt(idx, (char)(sb.charAt(idx)-1));
                                    break;
                            }
                    }
            }
            else {
                    while(idx>=0) {
                            if(sb.charAt(idx)=='9') {
                                    sb.setCharAt(idx, '0');
                                    idx--;
                            }
                            else {
                                    sb.setCharAt(idx, (char)(sb.charAt(idx)+1));
                                    break;
                            }
                    }
            }
            String mirror = mirrorLeft(sb.toString());
            return Math.abs(Long.valueOf(mirror)-x)< Math.abs(Long.valueOf(mirrorString)-x)?Long.valueOf(mirror): Long.valueOf(mirrorString);
    }
    private static String mirrorLeft(String x) {
            StringBuilder sb = new StringBuilder(x);
            for(int i = 0;i<x.length()/2;i++) {
                    sb.setCharAt(x.length()-1-i, x.charAt(i));
            }
            return sb.toString();
    }
	public static boolean canWinNim(int n) {
		count++;
        if(n<=3&&n>0)
            return true;
        if(canWinNim(n-1)==false)
            return true;
        else if(canWinNim(n-2)==false)
            return true;
        else if(canWinNim(n-3)==false)
            return true;
        return false;
    }
	public static int testException(int x) throws Exception{
		if(x>0)
			throw new Exception("sfd");
		else{
			return x;
		}
	}

	public static int atoi(String str) throws Exception {
        if(str==null)   
            return 0;
        if(str.length()==0||str.charAt(0)==' ')
        	throw new Exception("sfd");
        int isneg=1;
        int i=0;
        if(str.charAt(0)=='-'||str.charAt(0)=='+'){
            i++;
            if(str.charAt(0)=='-')
                isneg=-1;
        }
        int res=0;
        while(i<str.length()){
            if(str.charAt(i)<'0'||str.charAt(i)>'9')
                break;
            int digit=(int)(str.charAt(i)-'0');
            if(isneg==-1&&res>-((Integer.MIN_VALUE+digit)/10))
                return Integer.MIN_VALUE;
            else if(isneg==1&&res>(Integer.MAX_VALUE-digit)/10)
                return Integer.MAX_VALUE;
            res=res*10+digit;
            i++;
        }
        return res*isneg;
    }
	public static void printBrinary(int num) {
		String res="";
		for(int i=0;i<32;i++){
			int temp=num&1;
			res=temp+res;
			num=num>>>1;
		}
		System.out.println(res);
	}
	public static boolean  isPow4(int n) {
		int count=0;
		while(n!=0){
			if((n&1)==1){
				count++;
				if(count>1)
					return false;
			}
			n=n>>1;
		}
		return (count&1)==1?true:false;
	}
	public static int myABS(int n) {
		if((n>>>31)==1)
			return ~(n-1);
		else
			return n;
	}
	public static int reverseBit(int n) {
		int res=0;
		while(n!=0){
			res=res<<1;
			if((n&1)==1){
				res=res|1;
			}
			n=n>>>1;
		}
		return res;
	}
	public static int countBits(int n) {
		int res=0;
		while(n!=0){
			res++;
			n=n&(n-1);
		}
		return res;
	}
	public static boolean isPowerOfTwo(int n) {
		return (n&(n-1))==0;
		
	}
}
