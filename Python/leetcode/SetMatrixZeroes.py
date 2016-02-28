'''
Created on 1.12.2016

@author: Darren
''''''

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.


click to show follow up.

Follow up:


Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

" 
'''
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
        row_flag,col_flag=False,False
        for row in range(len(matrix)):
            if matrix[row][0]==0:
                row_flag=True
                break
        for col in range(len(matrix[0])):
            if matrix[0][col]==0:
                col_flag=True
                break
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col]==0:
                    matrix[row][0]=0
                    matrix[0][col]=0
        for row in range(1,len(matrix)):
            for col in range(1,len(matrix[0])):
                if matrix[0][col]==0 or matrix[row][0]==0:
                    matrix[row][col]=0
        if row_flag:
            for row in range(len(matrix)):
                matrix[row][0]=0
        if col_flag:
            for col in range(len(matrix[0])):
                matrix[0][col]=0
    def print_matrix(self,matrix):
        for line in matrix:
            print(line)
so=Solution()
matrix=[[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
so.print_matrix(matrix)
so.setZeroes(matrix)
print()
so.print_matrix(matrix)