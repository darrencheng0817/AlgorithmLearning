'''
Created on 1.12.2016

@author: Darren
''''''

Given an array of non-negative integers, you are initially positioned at the first index of the array.


Each element in the array represents your maximum jump length at that position. 


Determine if you are able to reach the last index.



For example:
A = [2,3,1,1,4], return true.


A = [3,2,1,0,4], return false.
" 
'''
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        reachable=0
        i=0
        while reachable>=i and i<len(nums):
            reachable=max(reachable,i+nums[i])
            i+=1
        return i==len(nums)