'''
Created on 1.12.2016

@author: Darren
''''''

Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T. 


The same repeated number may be chosen from C unlimited number of times.


Note:

All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, �� , ak) must be in non-descending order. (ie, a1 �� a2 �� �� �� ak).
The solution set must not contain duplicate combinations.




For example, given candidate set 2,3,6,7 and target 7, 
A solution set is: 
[7] 
[2, 2, 3] 

" 
'''
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates=sorted(candidates)
        res=[]
        def util(start,cur_sum,item):
            if cur_sum==target:
                res.append(item)
                return
            if cur_sum>target:
                return
            for index in range(start,len(candidates)):
                util(index,cur_sum+candidates[index],item+[candidates[index]])
        util(0,0,[])
        return res
            
                
so=Solution()
candidates=[2,3,6,7]
target=7
print(so.combinationSum(candidates, target))
