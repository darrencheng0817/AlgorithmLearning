/**
 * 
 */
package dp;

import java.util.concurrent.CountDownLatch;

/*
 Given a value N, if we want to make change for N cents, 
 and we have infinite supply of each of S = { S1, S2, .. , Sm} valued coins, 
 how many ways can we make the change? The order of coins doesn’t matter.

 For example, for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. 
 So output should be 4. For N = 10 and S = {2, 5, 3, 6}, 
 there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}. 
 So the output should be 5.*/

/**
 * @author Darren
 *
 */
public class CoinChange {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] coins = { 1, 5, 10, 25, 50 };
		System.out.println(count(coins, 100));
		System.out.println(count2(coins, 100));
	}

	static int count(int S[], int n) {
		int i, j, x, y;
		int m = S.length;
		// We need n+1 rows as the table is consturcted in bottom up manner
		// using
		// the base case 0 value case (n = 0)
		int[][] table = new int[n + 1][m];

		// Fill the enteries for 0 value case (n = 0)
		for (i = 0; i < m; i++)
			table[0][i] = 1;

		// Fill rest of the table enteries in bottom up manner
		for (i = 1; i < n + 1; i++) {
			for (j = 0; j < m; j++) {
				// Count of solutions including S[j]
				x = (i - S[j] >= 0) ? table[i - S[j]][j] : 0;

				// Count of solutions excluding S[j]
				y = (j >= 1) ? table[i][j - 1] : 0;

				// total count
				table[i][j] = x + y;
			}
		}
		return table[n][m - 1];
	}

	static int count2(int S[], int n) {
		// table[i] will be storing the number of solutions for
		// value i. We need n+1 rows as the table is consturcted
		// in bottom up manner using the base case (n = 0)
		int[] table = new int[n + 1];
		int m = S.length;

		// Base case (If given value is 0)
		table[0] = 1;

		// Pick all coins one by one and update the table[] values
		// after the index greater than or equal to the value of the
		// picked coin
		for (int i = 0; i < m; i++)
			for (int j = S[i]; j <= n; j++)
				table[j] += table[j - S[i]];

		return table[n];
	}
}
