'''
Created on 1.12.2016

@author: Darren
''''''
Given a collection of distinct numbers, return all possible permutations.


For example,

[1,2,3] have the following permutations:

[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].

" 
'''
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return [[n]+p for index,n in enumerate(nums) for p in self.permute(nums[:index]+nums[index+1:]) ] or [[]]

so=Solution()
print(so.permute([1,2,3]))
