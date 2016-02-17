'''
Created on 2016年2月16日

@author: Darren
'''
'''
Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:
Return true if there exists i, j, k 
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Your algorithm should run in O(n) time complexity and O(1) space complexity.

Examples:
Given [1, 2, 3, 4, 5],
return true.

Given [5, 4, 3, 2, 1],
return false.
'''
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        num1,num2=nums[0],max(nums)
        for i in range(1,len(nums)):
            if nums[i]>num2:
                return True
            if nums[i]>num1 and nums[i]<num2:
                num2=nums[i]
            if nums[i]<num1:
                num1=nums[i]
        return False