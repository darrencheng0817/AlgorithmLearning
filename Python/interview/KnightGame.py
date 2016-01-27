'''
Created on 2016年1月26日

@author: Darren
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
input:
    row col
    startpoint
    endpoint
    blockCount
    blocks
example
10 10
1 1
0 0
0

10 10
0 0
4 0
2
2 0
2 1
output
the min step required for knight to go from start point to end point 
'''
from collections import deque
def getResult(board,startPoint,endPoint):
    nextMoveI=[-2,-2,+2,+2,1,1,-1,-1]
    nextMoveJ=[1,-1,1,-1,2,-2,2,-2]
    queue=deque()
    queue.append(startPoint)
    visited=set()
    visited.add(startPoint)
    level=0
    while queue:
        newQueue=deque()
        level+=1
        while queue:
            i,j=queue.popleft()
            if (i,j)==endPoint:
                return level-1
            for index in range(8):
                nextI=i+nextMoveI[index]
                nextJ=j+nextMoveJ[index]
                if nextI>=0 and nextI<len(board) and nextJ<len(board[0]) and nextJ>=0 and not board[nextI][nextJ] and (nextI,nextJ) not in visited:
                    newQueue.append((nextI,nextJ))
                    visited.add((nextI,nextJ))
        queue=newQueue
    return 0
 
def solution():
    line1=input().strip().split(" ")
    rows,cols=int(line1[0]),int(line1[1])
    line2=input().strip().split(" ") 
    startPoint=(int(line2[0]),int(line2[1]))
    line3=input().strip().split(" ") 
    endPoint=(int(line3[0]),int(line3[1]))
    line4=input().strip()
    board=[[False]*cols for _ in range(rows)]
    for count in range(int(line4)):
        block=input().strip().split(" ")
        board[int(block[0])][int(block[1])]=True
    res=getResult(board,startPoint,endPoint)
    print(res)
 
solution()