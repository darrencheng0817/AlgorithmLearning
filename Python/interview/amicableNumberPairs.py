'''
Created on 2015年12月1日
找Amicable Number Pairs.
就是 数A 的所有因数(包括1，不包括A) 之和 等于 B。B的所有因数之和又刚好为A。 且 A != B.
求[1, N] 中所有符合条件的pair
@author: Darren
'''


def sum_of_div(num):
    i=2
    res=1
    while i*i<num:
        if num%i==0:
            res=res+i+num//i
        i+=1
    if i*i==num:
        res+=i
    return res

def isAmicable(num1,num2):
    if num1!=num2 and sum_of_div(num1)==num2 and sum_of_div(num2)==num1:
        return True
    return False

def printAmicableNumber(maxRange):
    for num1 in range(maxRange-1):
        for num2 in range(num1+1,maxRange):
            if isAmicable(num1, num2):
                print(str(num1)+" " +str(num2))
                

def printAmicableNumber2(maxRange):
    divSum=[1]*maxRange
    for i in range(2,maxRange):
        k=i+i
        while k<maxRange:
            divSum[k]+=i 
            k+=i
    for i in range(2,maxRange):
        if divSum[i]<maxRange and divSum[divSum[i]]==i and i<divSum[i]:
            print(str(i)+" "+str(divSum[i]))
printAmicableNumber2(1000000)