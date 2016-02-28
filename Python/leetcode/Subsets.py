'''
Created on 1.12.2016

@author: Darren
''''''

Given a set of distinct integers, nums, return all possible subsets.

Note:

Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.



For example,
If nums = [1,2,3], a solution is:



[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
" 
'''
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[[]]
        if not nums:
            return res
        nums=sorted(nums)
        for num in nums:
            new_items=[]
            for item in res:
                new_items.append(item+[num])
            res+=new_items
        return res