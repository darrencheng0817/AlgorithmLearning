'''
Created on 1.12.2016

@author: Darren
''''''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time." 
'''
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        dp=[0]*len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if j==0:
                    dp[j]+=grid[i][j]
                elif i==0:
                    dp[j]=dp[j-1]+grid[i][j]
                else:
                    dp[j]=min(dp[j],dp[j-1])+grid[i][j]
        return dp[-1]