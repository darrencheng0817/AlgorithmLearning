'''
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''


from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums.sort()
        preL = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                preL = len(res)
            for j in range(len(res) - preL, len(res)):
                    res.append(res[j] + [nums[i]])
        return res

s = Solution()
print(s.subsetsWithDup([1,2,2]))