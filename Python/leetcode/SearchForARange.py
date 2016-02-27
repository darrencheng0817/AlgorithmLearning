'''
Created on 1.12.2016

@author: Darren
''''''
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm s runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].


For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
" 
'''
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res=[-1,-1]
        if not nums:
            return res
        l,r=0,len(nums)-1
        while l<=r:
            m=(l+r)//2
            if nums[m]<target:
                l=m+1
            else:
                r=m-1
        res[0]=r+1
        l,r=0,len(nums)-1
        while l<=r:
            m=(l+r)//2
            if nums[m]<=target:
                l=m+1
            else:
                r=m-1
        res[1]=l-1
        if res[1]>=res[0]:
            return res
        else:
            return [-1,-1]