'''
Created on 2016年1月8日

@author: Darren
'''
'''
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2

'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res=[-1,-1]
        if not nums or len(nums)<2:
            return res
        d={}
        for index in range(len(nums)):
            if nums[index] in d:
                res[0]=d[nums[index]]+1
                res[1]=index+1
                return res
            d[target-nums[index]]=index
        return res