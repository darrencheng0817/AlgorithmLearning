'''
Created on 2016年1月8日

@author: Darren
'''
'''
Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

Example 1:
Given nums = [1, -1, 5, -2, 3], k = 3,
return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)

Example 2:
Given nums = [-2, -1, 2, 1], k = 1,
return 2. (because the subarray [-1, 2] sums to 1 and is the longest)

'''
class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s,res=0,0
        d={}
        for index in range(len(nums)):
            s+=nums[index]
            if s==k:
                res=index+1
            if s-k in d:
                res=max(res,index-d[s-k])
            if s not in d:
                d[s]=index
        return res
    
so=Solution()
nums=[1,-1,5,-2,3]
k=3
print(so.maxSubArrayLen(nums, k))