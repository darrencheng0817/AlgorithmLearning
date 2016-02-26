'''
Created on 1.12.2016

@author: Darren
'''
'''
Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4].
'''
class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums)<2:
            return
        i=1
        while i<len(nums):
            if nums[i-1]>nums[i]:
                nums[i-1],nums[i]=nums[i],nums[i-1]
            i+=1
            if i<len(nums) and nums[i-1]<nums[i]:
                nums[i-1],nums[i]=nums[i],nums[i-1]
            i+=1
        
so=Solution()
nums=[3, 5, 2, 1, 6, 4]
so.wiggleSort(nums)
print(nums)