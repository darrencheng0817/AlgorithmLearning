/**
 * 
 */
package dp;

/*Given a sequence, find the length of the longest palindromic subsequence in it. 
 * For example, if the given sequence is “BBABCBCAB”, then the output should be 7 
 * as “BABCBAB” is the longest palindromic subseuqnce in it. 
 * “BBBBB” and “BBCBB” are also palindromic subsequences of the given sequence, 
 * but not the longest ones.*/
/**
 * @author Darren
 *
 */
public class LPS {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		String testString="gphyvqruxjmwhonjjrgumxjhfyupajxbjgthzdvrdqmdouuukeaxhjumkmmhdglqrrohydrmbvtuwstgkobyzjjtdtjroqpyusfsbjlusekghtfbdctvgmqzeybnwzlhdnhwzptgkzmujfldoiejmvxnorvbiubfflygrkedyirienybosqzrkbpcfidvkkafftgzwrcitqizelhfsruwmtrgaocjcyxdkovtdennrkmxwpdsxpxuarhgusizmwakrmhdwcgvfljhzcskclgrvvbrkesojyhofwqiwhiupujmkcvlywjtmbncurxxmpdskupyvvweuhbsnanzfioirecfxvmgcpwrpmbhmkdtckhvbxnsbcifhqwjjczfokovpqyjmbywtpaqcfjowxnmtirdsfeujyogbzjnjcmqyzciwjqxxgrxblvqbutqittroqadqlsdzihngpfpjovbkpeveidjpfjktavvwurqrgqdomiibfgqxwybcyovysydxyyymmiuwovnevzsjisdwgkcbsookbarezbhnwyqthcvzyodbcwjptvigcphawzxouixhbpezzirbhvomqhxkfdbokblqmrhhioyqubpyqhjrnwhjxsrodtblqxkhezubprqftrqcyrzwywqrgockioqdmzuqjkpmsyohtlcnesbgzqhkalwixfcgyeqdzhnnlzawrdgskurcxfbekbspupbduxqxjeczpmdvssikbivjhinaopbabrmvscthvoqqbkgekcgyrelxkwoawpbrcbszelnxlyikbulgmlwyffurimlfxurjsbzgddxbgqpcdsuutfiivjbyqzhprdqhahpgenjkbiukurvdwapuewrbehczrtswubthodv";
		System.out.println(lps(testString.toCharArray()));
		System.out.println(longestPalindromicSubsequence(testString));
		System.out.println(longestPalindromicSubString(testString));
	}
	static int lps(char[] str)
	{
	   int n = str.length;
	   int i, j, cl;
	   int[][] L=new int[n][n];  // Create a table to store results of subproblems
	 
	 
	   // Strings of length 1 are palindrome of lentgh 1
	   for (i = 0; i < n; i++)
	      L[i][i] = 1;
	 
	    // Build the table. Note that the lower diagonal values of table are
	    // useless and not filled in the process. The values are filled in a
	    // manner similar to Matrix Chain Multiplication DP solution (See
	    // http://www.geeksforgeeks.org/archives/15553). cl is length of
	    // substring
	    for (cl=2; cl<=n; cl++)
	    {
	        for (i=0; i<n-cl+1; i++)
	        {
	            j = i+cl-1;
	            if (str[i] == str[j] && cl == 2)
	               L[i][j] = 2;
	            else if (str[i] == str[j])
	               L[i][j] = L[i+1][j-1] + 2;
	            else
	               L[i][j] = Math.max(L[i][j-1], L[i+1][j]);
	        }
	    }
	 
	    return L[0][n-1];
	}
	
	static int longestPalindromicSubsequence(String s){
		int length=s.length();
		int[][] dp=new int[length][length];
		for(int i=0;i<length;i++){
			dp[i][i]=1;
		}
		for(int len=2;len<=length;len++){
			for(int i=0;i<length-len+1;i++){
				int j=i+len-1;
				if(len==2&&s.charAt(i)==s.charAt(j)){
					dp[i][j]=2;
				}
				else if(s.charAt(i)==s.charAt(j)){
					dp[i][j]=dp[i+1][j-1]+2;
				}
				else{
					dp[i][j]=Math.max(dp[i+1][j], dp[i][j-1]);
				}
			}
		}
		return dp[0][length-1];
	}
	static int longestPalindromicSubString(String s){
		int res=1;
		int length=s.length();
		boolean[][] dp=new boolean[length][length];
		for(int i=0;i<length;i++){
			dp[i][i]=true;
			if(i>1&&s.charAt(i)==s.charAt(i-1)){
				dp[i-1][i]=true;
				res=2;
			}
		}
		for(int len=3;len<length+1;len++){
			for(int i=0;i<length-len+1;i++){
				int j=i+len-1;
				if(dp[i+1][j-1]==true&&s.charAt(i)==s.charAt(j)){
					dp[i][j]=true;
					res=len;
				}
			}
		}
		return res;
	}
}
