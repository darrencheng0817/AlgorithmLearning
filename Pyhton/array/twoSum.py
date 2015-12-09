'''
Created on 2015.11.30
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2

@author: Darren
'''
def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    map={}
    for i in range(len(nums)):
        if nums[i] in map:
            return map[nums[i]]+1,i+1
        else:
            map[target-nums[i]]=i
    return -1,-1