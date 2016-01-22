'''
Created on 2016年1月21日

@author: Darren
'''
from math import floor,ceil,log,sqrt
from timeit import Timer
def  superPower( z):
    for p in range(2,floor(sqrt(z))+1):
        for q in range(ceil(log(z)//log(p)),1,-1):
            if pow(p,q)==z:
                return 1
    return 0
def  superPower2( z):
    for p in range(2,floor(sqrt(z))+1):
        for q in range(2,ceil(log(z)//log(p))+1):
            if pow(p,q)==z:
                return 1
    return 0

def mytest1():
    superPower(pow(275,56))
def mytest2():
    superPower(pow(275,56))

t1=Timer('mytest1()', 'from __main__ import mytest1')
t2=Timer('mytest2()', 'from __main__ import mytest2')

print(t1.timeit(1))
print(t2.timeit(1))