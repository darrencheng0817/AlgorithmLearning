'''
Created on 1.12.2016

@author: Darren
''''''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.


Here are few examples.
[1,3,5,6], 5 &#8594; 2
[1,3,5,6], 2 &#8594; 1
[1,3,5,6], 7 &#8594; 4
[1,3,5,6], 0 &#8594; 0
" 
'''
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        l,r=0,len(nums)-1
        while l<=r:
            m=(l+r)//2
            if nums[m]==target:
                return m
            elif nums[m]<target:
                l=m+1
            else:
                r=m-1
        return l