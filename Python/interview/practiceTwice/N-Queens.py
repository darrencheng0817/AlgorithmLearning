'''
Created on 2015年12月1日
https://leetcode.com/problems/n-queens-ii/
@author: Darren
'''

def NQueens(N):
    pass

def printBoard(board):
    board2D=[["*"]*len(board) for i in range(len(board))]
    for row in range(len(board)):
        board2D[row][board[row]]="O"
        print(" ".join(board2D[row]))


res=NQueens(4)
for item in res:
    printBoard(item)
    print("")
    