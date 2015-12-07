'''
Created on 2015年12月1日
8*8 棋盘。输入起始点，终止点，和整数k，问从起始点到终止点走k步，有多少
种走法。

@author: Darren
'''
from timeit import Timer


def numOfWays(starti,startj,endi,endj,k):
    chessboard=[[0]*8 for i in range(8)]
    queue=[(starti,startj)]
    for step in range(k):
        newqueue=[]
        while queue:
            pointi,pointj=queue.pop(0)
            if pointi+1<8:
                newqueue.append((pointi+1,pointj))
            if pointi-1>=0:
                newqueue.append((pointi-1,pointj))
            if pointj+1<8:
                newqueue.append((pointi,pointj+1))
            if pointj-1>=0:
                newqueue.append((pointi,pointj-1))
        queue=newqueue
    return queue.count((endi,endj))

def numOfWays2(starti,startj,endi,endj,k):
    chessboard=[[0]*8 for i in range(8)]
    stack=[(starti,startj,0)]
    res=0
    while stack:
        pointi,pointj,level=stack.pop()
        if level==k:
            if pointi==endi and pointj==endj:
                res+=1
            continue
        if pointi+1<8:
            stack.append((pointi+1,pointj,level+1))
        if pointi-1>=0:
            stack.append((pointi-1,pointj,level+1))
        if pointj+1<8:
            stack.append((pointi,pointj+1,level+1))
        if pointj-1>=0:
            stack.append((pointi,pointj-1,level+1))
    return res

def numOfWays3(starti,startj,endi,endj,k):
    chessboard=[[0]*10 for i in range(10)]
    chessboard[starti+1][startj+1]=1
    for step in range(k):
        newBoard=[[0]*10 for i in range(10)]
        for i in range(1,9):
            for j in range(1,9):
                    newBoard[i][j]=chessboard[i][j-1]+chessboard[i][j+1]+chessboard[i-1][j]+chessboard[i+1][j]
        chessboard=newBoard
    return chessboard[endi+1][endj+1]



print(numOfWays(3,4,3,5,9))
print(numOfWays2(3,4,3,5,9))
print(numOfWays3(3,4,3,5,9))
def mytest1():
    numOfWays(3,4,3,5,9)
def mytest2():
    numOfWays2(3,4,3,5,9)
def mytest3():
    numOfWays3(3,4,3,5,9)
t1=Timer('mytest1()', 'from __main__ import mytest1')
t2=Timer('mytest2()', 'from __main__ import mytest2')
t3=Timer('mytest3()', 'from __main__ import mytest3')

print(t1.timeit(10))
print(t2.timeit(10))
print(t3.timeit(10))