'''
Created on 1.12.2016

@author: Darren
''''''
Given an array of size n, find the majority element. 
The majority element is the element that appears more than &lfloor; n/2 &rfloor; times.
You may assume that the array is non-empty and the majority element always exist in the array.
'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cand,c=nums[0]-1,0
        for i in range(0,len(nums)):
            if c==0:
                cand=nums[i]
                c=1
            else:
                if cand==nums[i]:
                    c+=1
                else:
                    c-=1
        return cand
                    