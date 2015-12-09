'''
Created on 2015年12月1日
https://leetcode.com/problems/n-queens-ii/
@author: Darren
'''

def NQueens(N):
    board=[-1]*N
    res=[]
    NQueensUtil(board, 0, res)
    return res
    
def check(board,row,col):
    if col in board:
        return False
    for i in range(row):
        if abs(i-row)==abs(col-board[i]):
            return False
    return True

def NQueensUtil(board,row,res):
    if row==len(board):
        res.append(list(board))
        return
    for col in range(len(board)):
        if check(board,row,col):
            board[row]=col
            NQueensUtil(board, row+1, res)
            board[row]=-1

def printBoard(board):
    board2D=[["*"]*len(board) for i in range(len(board))]
    for row in range(len(board)):
        board2D[row][board[row]]="O"
        print(" ".join(board2D[row]))


res=NQueens(4)
for item in res:
    printBoard(item)
    print("")
    