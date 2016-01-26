'''
Created on 1.12.2016

@author: Darren
''''''
The n-queens puzzle is the problem of placing n queens on an n��n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens  placement, where  Q  and  .  both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
" 
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


res=NQueens(14)
print(len(res))
# for item in res:
#     printBoard(item)
#     print("")