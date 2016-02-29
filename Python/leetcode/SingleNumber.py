'''
Created on 1.12.2016

@author: Darren
''''''
Given an array of integers, every element appears twice except for one. Find that single one.


Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
" 
'''
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=0
        for num in nums:
            res^=num
        return res