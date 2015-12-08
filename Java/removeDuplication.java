
public class removeDuplication {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int[] nums={1,1,4,4,4,5,5,6,6,6};
		System.out.println(remove(nums));
	}
	private static int remove(int[] nums) {
        if(nums==null||nums.length==0)
            return 0;
        
        int count=0,pre=nums[0]-1,index=0;
        for(int i=0;i<nums.length;i++){
            if(nums[i]!=pre){
                nums[index++]=nums[i];
                count=1;
                pre=nums[i];
            }
            else{
                if(count<2){
                    nums[index++]=nums[i];
                    count++;
                }
                else{
                    count++;
                }
            }
        }
        return index;
    }

}
