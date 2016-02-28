'''
Created on 1.12.2016

@author: Darren
''''''

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.


For example, given the array [&#8722;2,1,&#8722;3,4,&#8722;1,2,1,&#8722;5,4],
the contiguous subarray [4,&#8722;1,2,1] has the largest sum = 6.


click to show more practice.

More practice:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
" 
'''
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if max(nums)<0:
            return max(nums)
        local_sum,global_sum=0,0
        for num in nums:
            local_sum+=num
            if local_sum<0:
                local_sum=0
            global_sum=max(global_sum,local_sum)
        return global_sum
so=Solution()
nums=[-2,1,-3,4,-1,2,1,-5,4]
print(so.maxSubArray(nums))