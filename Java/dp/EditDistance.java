/**
 * 
 */
package dp;

/**
 * @author Darren
 *
 */
public class EditDistance {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		String s1="acbdf";
		String s2="dfa";
		System.out.println(editDistance(s1, s2));
	}

	static int editDistance(String s1,String s2){
		String longString=s1.length()>s2.length()?s1:s2;
		String shortString= s1.length()<=s2.length()?s1:s2;
		int[] dp=new int[shortString.length()+1];
		for(int i=0;i<shortString.length();i++){
			dp[i]=i;
		}
		for(int i=0;i<longString.length();i++){
			int[] newDp=new int[shortString.length()+1];
			newDp[0] = i+1;  
			for(int j=0;j<shortString.length();j++){
				if(longString.charAt(i)==shortString.charAt(j))
					newDp[j+1]=dp[j];
				else{
					newDp[j+1]=Math.min(dp[j], Math.min(dp[j+1], newDp[j]))+1;
				}
			}
			dp=newDp;
		}
		return dp[shortString.length()];
	}
}
