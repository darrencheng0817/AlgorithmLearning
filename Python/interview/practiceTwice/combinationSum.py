'''
Created on 2015年12月1日
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 2,3,6,7 and target 7, 
A solution set is: 
[7] 
[2, 2, 3] 
https://leetcode.com/problems/combination-sum/

@author: Darren
'''

def combinationSum(nums,target):
    '''
    :type: nums:list[int] target:int
    :rtype: list[list[int]]
    '''
    res=[]
    combinationSumUtil(nums, target, res, [], 0)
    return res

def combinationSumUtil(nums,target,res,item,index):
    if target==0:
        res.append(item)
        return
    if index>=len(nums) or target<0:
        return 
    for i in range(index,len(nums)):
        combinationSumUtil(nums, target-nums[i], res, item+[nums[i]], i+1)
        
print(combinationSum([1,4,2,3], 6))
