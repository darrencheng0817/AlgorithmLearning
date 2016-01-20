'''
Created on 1.12.2016

@author: Darren
''''''

Given a collection of numbers that might contain duplicates, return all possible unique permutations.
For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].
" 
'''
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]
        res=[[]]
        nums=sorted(nums)
        for n in nums:
            newList=[]
            for item in res:
                for index in range(len(item)+1):
                    newList.append(item[:index]+[n]+item[index:])
                    if index<len(item) and item[index]==n:
                        break
            res=newList
        return res

so=Solution()
print(so.permute([1,2,2]))