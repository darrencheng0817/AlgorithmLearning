'''
Created on 2015年12月1日
http://www.geeksforgeeks.org/find-the-longest-path-in-a-matrix-with-given-constraints/
@author: Darren
'''

def findPath(matrix):
    if not matrix or not matrix[0]:
        return 
    dp=[[0]*len(matrix[0]) for i in range(len(matrix))]
    res=0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            res=max(res,findPathUtil(matrix, dp, i, j))
    print(dp)
    return res

def findPathUtil(matrix,dp,i,j):
    if i<0 or i> len(matrix)-1 or j<0 or j>len(matrix[0])-1:
        return 0
    if dp[i][j]!=0:
        return dp[i][j]
    if i-1>=0 and matrix[i-1][j]==matrix[i][j]+1:
        dp[i][j]=findPathUtil(matrix, dp, i-1, j)+1
        return dp[i][j]
    if i+1<len(matrix) and matrix[i+1][j]==matrix[i][j]+1:
        dp[i][j]=findPathUtil(matrix, dp, i+1, j)+1
        return dp[i][j]
    if j-1>=0 and matrix[i][j-1]==matrix[i][j]+1:
        dp[i][j]=findPathUtil(matrix, dp, i, j-1)+1
        return dp[i][j]
    if j+1<len(matrix[0]) and matrix[i][j+1]==matrix[i][j]+1:
        dp[i][j]=findPathUtil(matrix, dp, i, j+1)+1  
        return dp[i][j]
    dp[i][j]=1
    return dp[i][j]
        
matrix=[[1,2,9],
        [5,3,8],
        [4,6,7]]
print(findPath(matrix))