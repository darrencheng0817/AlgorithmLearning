'''
Created on 2016年1月22日
gambing strategy: if I lose, I would double my stake
@author: Darren
'''
from random import random
from tkinter.constants import RIGHT

def play():
    stake=1
    targetProfit=1000000
    profit=0
    moneyRequied=0
    timeCount=0
    while profit<targetProfit:
        timeCount+=1
        moneyGet=0
        profit-=stake
        moneyRequied=max(moneyRequied,-profit)
        if random()>0.5:
            moneyGet+=stake*2
#             stake=1
        else:
            stake*=2
        profit+=moneyGet
        
    return (timeCount,moneyRequied)

def play2():
    stake=1
    targetProfit=1000
    profit=0
    moneyRequied=0
    timeCount=0
    while profit<targetProfit:
        timeCount+=1
        moneyGet=0
        profit-=stake
        moneyRequied=max(moneyRequied,-profit)
        if moneyRequied>1:
            return (timeCount,moneyRequied)
        if random()>0.5:
            moneyGet+=stake*2
#             stake=1
        else:
            stake*=2
        profit+=moneyGet
        
    return (timeCount,moneyRequied)

def playMul(times):
    timeCounts=[]
    moneySpents=[]
    for i in range(times):
        timeCount,moneyRequied=play()
        timeCounts.append(timeCount)
        moneySpents.append(moneyRequied)
    print(timeCounts)
    print(moneySpents)
    print(max(timeCounts))
    print(max(moneySpents))
    print(min(timeCounts))
    print(min(moneySpents))
    print(sum(timeCounts)//len(timeCounts))
    print(sum(moneySpents)//len(moneySpents))

def findLucklyGuy():
    count=0
    while True:
        count+=1
        timeCount,moneyRequied=play2()
        if moneyRequied==1:
            return count
        
playMul(100)
print(findLucklyGuy())