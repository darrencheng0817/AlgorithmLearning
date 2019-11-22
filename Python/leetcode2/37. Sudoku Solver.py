'''

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.

Note:

The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.

'''
from typing import List
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.helper(board, 0, 0)
        return board

    def helper(self, board, row, col):
        if row == len(board) -1 and col == len(board):
            return True
        if col == len(board):
            row = row + 1
            col = 0
        if board[row][col] == '.':
            for num in range(1, 10):
                if self.check(board, row, col, str(num)):
                    board[row][col] = str(num)
                    if self.helper(board, row, col+1):
                        return True
                    board[row][col] = '.'
        else:
            if self.helper(board, row , col + 1):
                return True


    def check(self, board, row, col, num):
        for j in range(len(board)):
            if board[row][j] == num:
                return False
        for i in range(len(board)):
            if board[i][col] == num:
                return False
        for i in range(3):
            for j in range(3):
                if board[row // 3 * 3 + i][col // 3 * 3 + j] == num:
                    return False
        return True

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
s = Solution()
s.solveSudoku(board)
print(board)