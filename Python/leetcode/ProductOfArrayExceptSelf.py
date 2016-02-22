'''
Created on 1.12.2016

@author: Darren
''''''

Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity? (Note: The output array does not count as extra space for the purpose of space complexity analysis.)" 
'''
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums or len(nums)==1:
            return nums
        res=[1]*len(nums)
        for index in range(1,len(nums)):
            res[index]=res[index-1]*nums[index-1]
        helper=1
        for index in range(len(nums)-1,-1,-1):
            res[index]*=helper
            helper*=nums[index]
        return res
so=Solution()
nums=[2,3]
print(so.productExceptSelf(nums))