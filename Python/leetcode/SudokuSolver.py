'''
Created on 1.12.2016

@author: Darren
''''''
Write a program to solve a Sudoku puzzle by filling the empty cells.
Empty cells are indicated by the character  . .
You may assume that there will be only one unique solution.
A sudoku puzzle...
...and its solution numbers marked in red.
" 
'''

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def util(i,j):
            if j==len(board):
                i+=1
                j=0
            if i==len(board):
                return True
            if board[i][j]==".":
                for candidate in range(1,10):
                    if check(i,j,str(candidate)):
                        board[i][j]=str(candidate)
                        if util(i,j+1):
                            return True
                        board[i][j]="."
            else:
                return util(i,j+1)
            return False
        
        def check(i,j,cand):
            for index in range(9):
                if board[i][index]==cand:
                    return False
            for index in range(9):
                if board[index][j]==cand:
                    return False
            for index_i in range(i//3*3,i//3*3+3):
                for index_j in range(j//3*3,j//3*3+3):
                    if board[index_i][index_j]==cand:
                        return False
            return True
        return util(0,0)
    
class Solution2(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        self.solveUtil(board,0,0)
    
    
    def solveUtil(self,board,i,j):
        if j>=9:
            return self.solveUtil(board,i+1,0)
        if i==9:
            return True
        if board[i][j]=='.':
            for k in range(1,10):
                board[i][j]=str(k)
                if self.isValid(board,i,j):
                    if self.solveUtil(board,i,j+1):
                        return True
                board[i][j]='.'
        else:
            return self.solveUtil(board,i,j+1)
#         return False
    
    def isValid(self,board,i,j):
        for row in range(9):
            if row!=i and board[i][j]==board[row][j]:
                return False
        for col in range(9):
            if col!=j and board[i][j]==board[i][col]:
                return False
        for row in range(i//3*3,i//3*3+3):
            for col in range(j//3*3,j//3*3+3):
                if (row!=i or col!=j) and board[row][col]==board[i][j]:
                    return False
        return True
                   
board=["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."] 
for index in range(len(board)):
    board[index]=list(board[index])
so=Solution()
print(so.solveSudoku(board))
print(board)