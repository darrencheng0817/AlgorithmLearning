'''
Created on 1.12.2016

@author: Darren
''''''

Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.


Do not allocate extra space for another array, you must do this in place with constant memory.



For example,
Given input array nums = [1,1,2],


Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn t matter what you leave beyond the new length.
" 
'''
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        pointer,pre=0,None
        for index,num in enumerate(nums):
            if num!=pre:
                pre=num
                nums[pointer]=num
                pointer+=1
        return pointer
