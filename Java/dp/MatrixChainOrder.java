/**
 * 
 */
package dp;

/*Given an array p[] which represents the chain of matrices such that the ith matrix Ai is of dimension p[i-1] x p[i].
 *  We need to write a function MatrixChainOrder() that should 
 *  return the minimum number of multiplications needed to multiply the chain.

  Input: p[] = {40, 20, 30, 10, 30}   
  Output: 26000  
  There are 4 matrices of dimensions 40x20, 20x30, 30x10 and 10x30.
  Let the input 4 matrices be A, B, C and D.  The minimum number of 
  multiplications are obtained by putting parenthesis in following way
  (A(BC))D --> 20*30*10 + 40*20*10 + 40*10*30

  Input: p[] = {10, 20, 30, 40, 30} 
  Output: 30000 
  There are 4 matrices of dimensions 10x20, 20x30, 30x40 and 40x30. 
  Let the input 4 matrices be A, B, C and D.  The minimum number of 
  multiplications are obtained by putting parenthesis in following way
  ((AB)C)D --> 10*20*30 + 10*30*40 + 10*40*30

  Input: p[] = {10, 20, 30}  
  Output: 6000  
  There are only two matrices of dimensions 10x20 and 20x30. So there 
  is only one way to multiply the matrices, cost of which is 10*20*30

 * */


/**
 * @author Darren
 *
 */
public class MatrixChainOrder {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		int arr[] = {40, 20, 30, 10, 30} ;
		System.out.println(matrixChainOrder(arr));

	}
	static int matrixChainOrder(int[] chain){
		int n=chain.length;
		int[][] dp=new int[n][n];
		/* dp[i,j] = Minimum number of scalar multiplications needed to compute
	       the matrix A[i]A[i+1]...A[j] = A[i..j] where dimention of A[i] is
	       p[i-1] x p[i] */
	 
	    // cost is zero when multiplying one matrix.
		for(int i=0;i<n;i++){
			for(int j=0;j<n;j++)
				if(i==j)
					dp[i][j]=0;
				else
					dp[i][j]=Integer.MAX_VALUE;
		}
		// L is chain length.
		for(int L=2;L<n;L++){
			for(int i=1;i<n-L+1;i++){
				int j=i+L-1;
				for(int k=i;k<=j-1;k++){
					int q = dp[i][k] + dp[k+1][j] + chain[i-1]*chain[k]*chain[j];
					if(q<dp[i][j])
						dp[i][j]=q;
				}
			}
		}
		return dp[1][n-1];
	}

}
