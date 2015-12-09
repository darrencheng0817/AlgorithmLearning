/**
 * 
 */
package dp;

/**
 * @author Darren
 *
 */
public class LongestIncreasingSequence {
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		int[] array = { 6, 7, 2,8, 9, 1, 2, 3, 2, 3, 4, 5 };
		int[] res = new int[array.length];
		int lis = LISSEx(array, res);
		System.out.println(lis1(array));
		System.out.println(lis);
		printArray(res, lis);
	}

	private static void printArray(int[] res, int n) {
		for (int i = 0; i < n; i++) {
			System.out.println(res[i]);
		}
	}

	static int LISSEx(int array[], int result[]) {
		int i, j, k, l, max;
		int length = array.length;
		int[] liss = new int[length];
		// 前驱元素数组，用于打印序列
		int[] pre = new int[length];
		liss[0] = 0;
		for (i = 0; i < length; ++i) {
			pre[i] = i;
		}
		for (i = 1, max = 1; i < length; ++i) {
			// 找到这样的j使得在满足array[liss[j]] > array[i]条件的所有j中，j最小
			j = 0;
			k = max - 1;
			while (k - j > 1) {
				l = (j + k) / 2;
				if (array[liss[l]] < array[i]) {
					j = l;
				} else {
					k = l;
				}
			}
			if (array[liss[j]] < array[i]) {
				j = k;
			}
			// array[liss[0]]的值也比array[i]大的情况
			if (j == 0) {
				// 此处必须加等号，防止array中存在多个相等的最小值时，将最小值填充到liss[1]位置
				if (array[liss[0]] >= array[i]) {
					liss[0] = i;
					continue;
				}
			}
			// array[liss[max -1]]的值比array[i]小的情况
			if (j == max - 1) {
				if (array[liss[j]] < array[i]) {
					pre[i] = liss[j];
					liss[max++] = i;
					continue;
				}
			}
			pre[i] = liss[j - 1];
			liss[j] = i;
		}
		// 输出递增子序列
		i = max - 1;
		k = liss[max - 1];
		while (pre[k] != k) {
			result[i--] = array[k];
			k = pre[k];
		}
		result[i] = array[k];
		return max;
	}

	static int lis1(int[] L) {
		int n = L.length;
		int[] B = new int[n + 1];// 数组B；
		B[0] = -10000;// 把B[0]设为最小，假设任何输入都大于-10000；
		B[1] = L[0];// 初始时，最大递增子序列长度为1的最末元素为a1
		int Len = 1;// Len为当前最大递增子序列长度，初始化为1；
		int p, r, m;// p,r,m分别为二分查找的上界，下界和中点；
		for (int i = 1; i < n; i++) {
			p = 0;
			r = Len;
			while (p <= r)// 二分查找最末元素小于ai+1的长度最大的最大递增子序列；
			{
				m = (p + r) / 2;
				if (B[m] < L[i])
					p = m + 1;
				else
					r = m - 1;
			}
			B[p] = L[i];// 将长度为p的最大递增子序列的当前最末元素置为ai+1;
			if (p > Len)
				Len++;// 更新当前最大递增子序列长度；

		}
		return Len;
	}
}
