'''
Created on 1.12.2016

@author: Darren
''''''

Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.


Each number in C may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, �� , ak) must be in non-descending order. (ie, a1 �� a2 �� �� �� ak).
The solution set must not contain duplicate combinations.




For example, given candidate set 10,1,2,7,6,1,5 and target 8, 
A solution set is: 
[1, 7] 
[1, 2, 5] 
[2, 6] 
[1, 1, 6] 
" 
'''
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
                if index>start and candidates[index]==candidates[index-1]:
                    continue
                util(index+1,cur_sum+candidates[index],item+[candidates[index]])
        util(0,0,[])
        return res