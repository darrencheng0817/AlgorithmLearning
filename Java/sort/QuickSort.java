/**
 * 
 */
package sort;

/**
 * @author Darren
 *
 */
public class QuickSort {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		int arr[] = {10, 7, 8, 9, 1, 5};
	    int n = arr.length;
	    quickSort(arr, 0, n-1);
	    printArray(arr);
	}

	private static void printArray(int[] arr) {
		for(int n:arr){
			System.out.println(n);
		}
	}

	static int partition3(int s[], int l, int r) //返回调整后基准数的位置
	{
		int i = l, j = r;
		int x = s[l]; //s[l]即s[i]就是第一个坑 
		while (i < j){
			// 从右向左找小于x的数来填s[i] 
			while(i < j && s[j] >= x)
				j--; 
			if(i < j){
				s[i] = s[j]; //将s[j]填到s[i]中,s[j]就形成了一个新的坑 i++;
			}
			// 从左向右找大于或等于x的数来填s[j] 
			while(i < j && s[i] < x)
				i++;
			if(i < j){
				s[j] = s[i]; //将s[i]填到s[j]中,s[i]就形成了一个新的坑 j--;
			} 
		}
		//退出时,i等于j。将x填到这个坑中。 
		s[i] = x;
		return i; 
	}
	
	
	/* This function takes first element as pivot, places the pivot element at its
	   correct position in sorted array, and places all smaller (smaller than pivot)
	   to left of pivot and all greater elements to right of pivot */
	static int partition2 (int arr[], int l, int h)
	{
	    int x = arr[l];    // pivot
	    int i = (l-1);  // Index of smaller element
	 
	    for (int j = l+1; j <= h; j++)
	    {
	        // If current element is smaller than or equal to pivot 
	        if (arr[j] <= x)
	        {
	            i++;    // increment index of smaller element
	            swap(arr,i,j);  // Swap current element with index
	        }
	    }
	    arr[i+1]=x;  
	    return (i + 1);
	}
	
	/* This function takes last element as pivot, places the pivot element at its
	   correct position in sorted array, and places all smaller (smaller than pivot)
	   to left of pivot and all greater elements to right of pivot */
	static int partition (int arr[], int l, int h)
	{
	    int x = arr[h];    // pivot
	    int i = (l - 1);  // Index of smaller element
	 
	    for (int j = l; j <= h- 1; j++)
	    {
	        // If current element is smaller than or equal to pivot 
	        if (arr[j] <= x)
	        {
	            i++;    // increment index of smaller element
	            swap(arr,i,j);  // Swap current element with index
	        }
	    }
	    swap(arr,i + 1, h);  
	    return (i + 1);
	}
	 
	static /* arr[] --> Array to be sorted, l  --> Starting index, h  --> Ending index */
	void quickSort(int arr[], int l, int h)
	{
	    if (l < h)
	    {
	        int p = partition3(arr, l, h); /* Partitioning index */
	        quickSort(arr, l, p - 1);
	        quickSort(arr, p + 1, h);
	    }
	}
	
	static void swap(int[] arr,int i,int j){
		int temp=arr[i];
		arr[i]=arr[j];
		arr[j]=temp;
	}
	
	
}
