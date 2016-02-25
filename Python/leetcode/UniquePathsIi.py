'''
Created on 1.12.2016

@author: Darren
''''''
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]

The total number of unique paths is 2.

Note: m and n will be at most 100." 
'''
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        dp=[0]*len(obstacleGrid[0])
        dp[0]=1
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j]==1:
                    dp[j]=0
                else:
                    if j>0:
                        dp[j]+=dp[j-1]
        return dp[-1]

so=Solution()
obstacleGrid=[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]

print(so.uniquePathsWithObstacles(obstacleGrid))