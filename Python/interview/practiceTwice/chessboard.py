'''
Created on 2015年12月1日
8*8 棋盘。输入起始点，终止点，和整数k，问从起始点到终止点走k步，有多少
种走法。

@author: Darren
'''


def numOfWays(starti,startj,endi,endj,k):
    BOARD_LENGTH=8
    dp=[[0]*(BOARD_LENGTH+2) for __temp in range(BOARD_LENGTH+2)]
    dp[starti+1][startj+1]=1
    step=0
    while step<k:
        newDp=[[0]*(BOARD_LENGTH+2) for __temp in range(BOARD_LENGTH+2)]
        for i in range(1,BOARD_LENGTH+1):
            for j in range(1,BOARD_LENGTH+1):
                newDp[i][j]=dp[i-1][j]+dp[i+1][j]+dp[i][j+1]+dp[i][j-1]
        dp=newDp
        step+=1
    return dp[endi+1][endj+1]

print(numOfWays(3,4,3,5,9))
