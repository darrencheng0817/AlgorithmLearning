'''
Created on 1.12.2016

@author: Darren
''''''

Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note:

Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.



For example,
If nums = [1,2,2], a solution is:



[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
" 
'''
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[[]]
        if not nums:
            return res
        nums=sorted(nums)
        pre=[]
        for index,num in enumerate(nums):
            if index>0 and num==nums[index-1]:
                seeds=pre
            else:
                seeds=res
            new_items=[]
            for item in seeds:
                new_items.append(item+[num])
            res+=new_items
            pre=new_items
        return res