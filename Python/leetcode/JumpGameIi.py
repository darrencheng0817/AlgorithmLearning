'''
Created on 1.12.2016

@author: Darren
'''
'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position. 

Your goal is to reach the last index in the minimum number of jumps.
For example:
Given array A = [2,3,1,1,4]
The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

Note:
You can assume that you can always reach the last index." 
'''
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        step,lastreach,reachable=0,0,nums[0]
        for i in range(len(nums)):
            if i>lastreach:
                step+=1
                lastreach=reachable
            reachable=max(reachable,i+nums[i])
        return step
so=Solution()
nums=[2,3,1,1,4]
print(so.jump(nums))