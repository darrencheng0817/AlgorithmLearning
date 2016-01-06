'''
Created on 2016年1月5日

@author: Darren
'''
'''
You want to build a house on an empty land which reaches all buildings in the shortest amount of distance. You can only move up, down, left and right. You are given a 2D grid of values 0, 1 or 2, where:

Each 0 marks an empty land which you can pass by freely.
Each 1 marks a building which you cannot pass through.
Each 2 marks an obstacle which you cannot pass through.
For example, given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2):

1 - 0 - 2 - 0 - 1
|   |   |   |   |
0 - 0 - 0 - 0 - 0
|   |   |   |   |
0 - 0 - 1 - 0 - 0
The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal. So return 7.

Note:
There will be at least one building. If it is not possible to build such house according to the above rules, return -1.
'''
class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dp=[[0]*len(grid[0]) for i in range(len(grid))]
        connected=[[0]*len(grid[0]) for i in range(len(grid))]
        num=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    queue=[(i,j)]
                    num+=1
                    visited=set((i,j))
                    count=1
                    level=1
                    while queue:
                        curi,curj=queue.pop(0)
                        count-=1
                        if curi-1>=0 and (curi-1,curj) not in visited and grid[curi-1][curj]==0:
                            queue.append((curi-1,curj))
                            dp[curi-1][curj]+=level
                            visited.add((curi-1,curj))
                            connected[curi-1][curj]+=1
                        if curi+1<len(grid) and (curi+1,curj) not in visited and grid[curi+1][curj]==0:
                            queue.append((curi+1,curj))
                            dp[curi+1][curj]+=level
                            visited.add((curi+1,curj))
                            connected[curi+1][curj]+=1
                        if curj-1>=0 and (curi,curj-1) not in visited and grid[curi][curj-1]==0:
                            queue.append((curi,curj-1))
                            dp[curi][curj-1]+=level
                            visited.add((curi,curj-1))
                            connected[curi][curj-1]+=1
                        if curj+1<len(grid[0]) and (curi,curj+1) not in visited and grid[curi][curj+1]==0:
                            queue.append((curi,curj+1))
                            dp[curi][curj+1]+=level
                            visited.add((curi,curj+1))
                            connected[curi][curj+1]+=1
                        if count==0:
                            level+=1
                            count=len(queue)
                    print(dp)
        res=len(grid)*len(grid[0])*len(grid)*len(grid[0])
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if dp[i][j]!=0 and dp[i][j]<res and connected[i][j]==num:
                    res=dp[i][j]
        return res if not res==len(grid)*len(grid[0])*len(grid)*len(grid[0]) else -1    
            
        
so=Solution()
grid=[[1,1,1,1,1,1,1,0],[0,0,0,0,0,0,0,1],[1,1,1,1,1,1,0,1],[1,0,0,0,1,1,0,1],[1,0,1,1,1,1,0,1],[1,0,1,0,0,1,0,1],[1,0,1,1,1,1,0,1],[1,0,0,0,0,0,0,1],[0,1,1,1,1,1,1,0]]
print(so.shortestDistance(grid))
