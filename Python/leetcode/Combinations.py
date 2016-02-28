'''
Created on 1.12.2016

@author: Darren
''''''

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.


For example,
If n = 4 and k = 2, a solution is:



[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
" 
'''
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res=[]
        def util(item,index):
            if len(item)==k:
                res.append(item)
                return
            if index>n:
                return
            for num in range(index+1,n+1):
                util(item+[num],num)
        util([],0)
        return res
        