'''
Created on 2015年12月1日
找Amicable Number Pairs.
就是 数A 的所有因数(包括1，不包括A) 之和 等于 B。B的所有因数之和又刚好为A。 且 A != B.
求[1, N] 中所有符合条件的pair
@author: Darren
'''

def printAmicableNumber(maxRange):
    dp=[1]*maxRange
    for i in range(2,maxRange):
        k=i+i
        while k<maxRange:
            dp[k]+=i
            k+=i
    for i in range(2,maxRange):
        if dp[i]<maxRange and dp[dp[i]]==i and i<dp[i]:
            print(str(i)+" "+str(dp[i]))
printAmicableNumber(1000000)