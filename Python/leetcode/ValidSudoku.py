'''
Created on 1.12.2016

@author: Darren
''''''
from Python.leetcode.BinaryTreePaths import Solution
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character  . .



A partially filled sudoku which is valid.


Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
" 
'''
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        l=len(board)
        for i in range(l):
            s=set()
            for j in range(l):
                if board[i][j] in s:
                    return False
                if board[i][j].isdigit():
                    s.add(board[i][j])
        for i in range(l):
            s=set()
            for j in range(l):
                if board[j][i] in s:
                    return False
                if board[j][i].isdigit():
                    s.add(board[j][i])
        for section in range(9):
            s=set()
            for i in range(section//3*3,section//3*3+3):
                for j in range(section%3*3,section%3*3+3):
                    if board[i][j] in s:
                        return False
                    if board[i][j].isdigit():
                        s.add(board[i][j])
        return True

board=["..5.....6","....14...",".........",".....92..","5....2...",".......3.","...54....","3.....42.","...27.6.."]
for line in board:
    print(' '.join(list(line)))
so=Solution()
print(so.isValidSudoku(board))