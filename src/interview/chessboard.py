'''
Created on 2015年12月1日
8*8 棋盘。输入起始点，终止点，和整数k，问从起始点到终止点走k步，有多少
种走法。

@author: Darren
'''


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

print(numOfWays(3,4,3,5,3))