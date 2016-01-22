'''
Created on 2016年1月21日
Gaven a string contains "W" and "B", you can change "W" to "B" at most k times, print the longest continuous streak of "B"
@author: Darren
'''
def  maxStreak( s,  k):
    interval=[]
    interval.append((0,0))
    index=0
    while index<len(s):
        if s[index] =="B":
            startIndex=index
            while index<len(s) and s[index]=="B":
                index+=1
            endIndex=index
            interval.append((startIndex,endIndex))
        index+=1
    interval.append((len(s),len(s)))
    interval.append((0,0))
    resStart,resEnd=0,0
    res=0
    for intervalIndex in range(len(interval)):
        startInterval,endInterval=intervalIndex,intervalIndex
        startIndex1,endIndex1=interval[startInterval]
        rest=k
        while rest>0 and endInterval<len(interval)-1:
            endInterval+=1
            startIndex2,endIndex2=interval[endInterval]
            if startIndex2-endIndex1<=rest:
                rest=rest-(startIndex2-endIndex1)
                if res<=endIndex2-startIndex1:
                    res=endIndex2-startIndex1
                    resStart,resEnd=startInterval,endInterval
                endIndex1=endIndex2
    print(res)
    res2=[]
    for index in range(resStart,resEnd):
        if interval[index][1]!=interval[index+1][0]:
            res2.append((interval[index][1],interval[index+1][0]))
    print(res2)
s="BBBBBBBBBBBBBBBBWBWWBWWBWWWWWWBBBBWWBWWWWWWWWWWWWBBBBBBBBBBB"
maxStreak(s, 4)