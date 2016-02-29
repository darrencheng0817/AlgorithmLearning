'''
Created on 1.12.2016

@author: Darren
''''''

Find the contiguous subarray within an array (containing at least one number) which has the largest product.



For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
" 
'''
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        res=nums[0]
        local_max,local_min=nums[0],nums[0]
        for i in range(1,len(nums)):
            temp=local_max
            local_max=max(nums[i],local_max*nums[i],local_min*nums[i])
            local_min=min(nums[i],temp*nums[i],local_min*nums[i])
            res=max(res,local_max)
        return res