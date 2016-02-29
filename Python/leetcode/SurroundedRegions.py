'''
Created on 1.12.2016

@author: Darren
''''''

Given a 2D board containing  X  and  O , capture all regions surrounded by  X .

A region is captured by flipping all  O s into  X s in that surrounded region.



For example,

X X X X
X O O X
X X O X
X O X X




After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

" 
'''
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return 
        queue=[]
        for i in [0,len(board)-1]:
            for j in range(len(board[0])):
                if board[i][j]=="O":
                    board[i][j]="B"
                    queue.append((i,j))
        for j in [0,len(board[0])-1]:
            for i in range(len(board)):
                if board[i][j]=="O":
                    board[i][j]="B"
                    queue.append((i,j))
        shifts=[(1,0),(-1,0),(0,1),(0,-1)]
        while queue:
            i,j=queue.pop()
            for shift_i,shift_j in shifts:
                new_i=i+shift_i
                new_j=j+shift_j
                if 0<=new_i<len(board) and 0<=new_j<len(board[0]) and board[new_i][new_j]=="O":
                    board[new_i][new_j]="B"
                    queue.append((new_i,new_j))
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=="O":
                    board[i][j]="X"
                elif board[i][j]=="B":
                    board[i][j]="O"
                
            
so=Solution()
board=["XOXOXO","OXOXOX","XOXOXO","OXOXOX"]
for index in range(len(board)):
    board[index]=list(board[index])
so.solve(board)
print(board)