'''
Created on 2015年12月1日
给出N个数字，不改变它们的相对位置，在中间加入K个乘号和N-K-1个加号，
（括号随便加）使最终结果尽量大。因为乘号和加号一共就是N-1个了，所以恰好每两个相邻数字之间都有一个符号。
http://www.lostscroll.com/max-value-using-and/
@author: Darren
'''
def maxValue(nums):
    dp=[[0]*len(nums) for i in range(len(nums)+1)]
    sumN=[0]*(len(nums)+1)
    for i in range(1,len(nums)+1):
        sumN[i]=sumN[i-1]+nums[i-1]
        dp[i][0]=sumN[i]
    res=dp[len(nums)][0]
    for i in range(2,len(nums)+1):
        for j in range(1,i):
            for k in range(j,i): 
                dp[i][j]=max(dp[i][j],dp[k][j-1]*(sumN[i]-sumN[k]))
            if i==len(nums) and dp[len(nums)][j]>res:
                res=dp[len(nums)][j]
    return res

def maxValue2(nums):
    pass

nums=[1,1,1,1,1,1,1,1,1]
print(maxValue(nums))
print(maxValue2(nums))