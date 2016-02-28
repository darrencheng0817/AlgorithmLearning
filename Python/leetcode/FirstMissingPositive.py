'''
Created on 1.12.2016

@author: Darren
''''''

Given an unsorted integer array, find the first missing positive integer.



For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.



Your algorithm should run in O(n) time and uses constant space.
" 
'''
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index=0
        while index<len(nums):
            if nums[index]>0 and nums[index]<=len(nums) and nums[nums[index]-1]!=nums[index]:
                nums[nums[index]-1],nums[index]=nums[index],nums[nums[index]-1]
#                 nums[index],nums[nums[index]-1]=nums[nums[index]-1],nums[index] this will not work, because nums[index] changed then num[nums[index]-1] is not what we want
            else:
                index+=1

        for index in range(len(nums)):
            if nums[index]!=index+1:
                return index+1
        return len(nums)+1

    
nums=[3,4,-1,1]
so=Solution()
print(so.firstMissingPositive(nums))