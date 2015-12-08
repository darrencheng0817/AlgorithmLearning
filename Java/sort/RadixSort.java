/**
 * 
 */
package sort;

/**
 * @author Darren
 *
 */
public class RadixSort {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int arr[] = {170, 45, 75, 90, 802, 24, 2, 66};
	    radixsort(arr);
	    print(arr);
	}
	/**
	 * @param arr
	 * @param n
	 * The main function to that sorts arr[] of size n using Radix Sort
	 */
	static void radixsort(int arr[])
	{
	    // Find the maximum number to know number of digits
	    int m = getMax(arr);
	 
	    // Do counting sort for every digit. Note that instead of passing digit
	    // number, exp is passed. exp is 10^i where i is current digit number
	    for (int exp = 1; m/exp > 0; exp *= 10)
	        countSort(arr, exp);
	}

	// A utility function to get maximum value in arr[]
	static int getMax(int arr[])
	{
		int n=arr.length;
	    int mx = arr[0];
	    for (int i = 1; i < n; i++)
	        if (arr[i] > mx)
	            mx = arr[i];
	    return mx;
	}
	
	// A function to do counting sort of arr[] according to
	// the digit represented by exp.
	static void countSort(int arr[], int exp)
	{
		int n=arr.length;
	    int[] output=new int[n];// output array
	    int[] count=new int[10]; 
	    int i;
	 
	    // Store count of occurrences in count[]
	    for (i = 0; i < n; i++)
	        count[ (arr[i]/exp)%10 ]++;
	 
	    // Change count[i] so that count[i] now contains actual position of
	    // this digit in output[]
	    for (i = 1; i < 10; i++)
	        count[i] += count[i - 1];
	 
	    // Build the output array
	    for (i = n - 1; i >= 0; i--)
	    {
	        output[count[ (arr[i]/exp)%10 ] - 1] = arr[i];
	        count[ (arr[i]/exp)%10 ]--;
	    }
	 
	    // Copy the output array to arr[], so that arr[] now
	    // contains sorted numbers according to curent digit
	    for (i = 0; i < n; i++)
	        arr[i] = output[i];
	}

	
	// A utility function to print an array
	static void print(int arr[])
	{
	    for (int i = 0; i < arr.length; i++)
	        System.out.println(arr[i]);
	}
}
