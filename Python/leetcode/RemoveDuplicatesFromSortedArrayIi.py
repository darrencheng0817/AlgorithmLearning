'''
Created on 1.12.2016

@author: Darren
''''''

Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?


For example,
Given sorted array nums = [1,1,1,2,2,3],


Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn t matter what you leave beyond the new length.
" 
'''
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums)<3:
            return len(nums)
        validIndex=2
        for index in range(2,len(nums)):
            if nums[index]==nums[validIndex-1] and nums[index]==nums[validIndex-2]:
                continue
            nums[validIndex]=nums[index]
            validIndex+=1
        return validIndex