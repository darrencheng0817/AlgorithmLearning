'''
Created on 1.12.2016

@author: Darren
''''''
Given n, how many structurally unique BST s (binary search trees) that store values 1...n?


For example,
Given n = 3, there are a total of 5 unique BST s.


   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

" 
'''
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=0:
            return 0
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1
        for i in range(2,n+1):
            for j in range(i):
                dp[i]+=dp[j]*dp[i-j-1]
        return dp[-1]