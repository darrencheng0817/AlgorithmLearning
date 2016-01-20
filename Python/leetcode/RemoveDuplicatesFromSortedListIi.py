'''
Created on 1.12.2016

@author: Darren
''''''

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.


For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
" 
'''
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums)<3:
            return nums
        validIndex=2
        for index in range(2,len(nums)):
            if nums[index]==nums[validIndex-1] and nums[index]==nums[validIndex-2]:
                continue
            nums[validIndex]=nums[index]
            validIndex+=1
        return validIndex
so=Solution()
nums=[]
print(so.removeDuplicates(nums))