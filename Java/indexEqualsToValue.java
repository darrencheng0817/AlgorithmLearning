
public class indexEqualsToValue {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] nums={-1,0,1,3,6,7,8};
		System.out.println(findIndex(nums));
		
	}
	private static int findIndex(int[] nums) {
		int l=0,r=nums.length-1;
		while(l<=r){
			int m=(l+r)/2;
			if(nums[m]==m){
				return m;
			}
			else if(nums[m]>m){
				r=m-1;
			}
			else{
				l=m+1;
			}
		}
		return 0;
	}
}

