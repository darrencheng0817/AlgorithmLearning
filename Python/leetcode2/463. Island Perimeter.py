'''
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.



Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

Explanation: The perimeter is the 16 yellow stripes in the image below:
'''

from queue import Queue
class Solution:
    def islandPerimeter(self, grid) -> int:
        if not grid:
            return 0
        visited = set()
        q = Queue()
        res = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    q.put((row,col))
                    visited.add((row, col))
                    while q.qsize() > 0:
                        i, j = q.get()
                        res += 4
                        c = 0

                        print("ori", i, j)
                        for di,dj in [(0,1),(1,0),(-1,0),(0,-1)]:
                            if 0<=i+di<len(grid) and 0<=j+dj<len(grid[0]) and grid[i+di][j+dj] == 1:
                                res -= 1
                                print(i+di, j+dj)
                                c+=1

                                if (i+di, j+dj) not in visited:
                                    q.put((i+di, j+dj))
                                    visited.add((i+di, j+dj))
                        print(c)
                if visited:
                    return res
        return res

s = Solution()
print(s.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))