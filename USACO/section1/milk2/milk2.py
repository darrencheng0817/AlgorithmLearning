'''
Created on 2016年2月9日

@author: Darren
'''
'''
Milking Cows
Three farmers rise at 5 am each morning and head for the barn to milk three cows. The first farmer begins milking his cow at time 300 (measured in seconds after 5 am) and ends at time 1000. The second farmer begins at time 700 and ends at time 1200. The third farmer begins at time 1500 and ends at time 2100. The longest continuous time during which at least one farmer was milking a cow was 900 seconds (from 300 to 1200). The longest time no milking was done, between the beginning and the ending of all milking, was 300 seconds (1500 minus 1200).

Your job is to write a program that will examine a list of beginning and ending times for N (1 <= N <= 5000) farmers milking N cows and compute (in seconds):

The longest time interval at least one cow was milked.
The longest time interval (after milking starts) during which no cows were being milked.
PROGRAM NAME: milk2

INPUT FORMAT

Line 1:    The single integer
Lines 2..N+1:    Two non-negative integers less than 1,000,000, respectively the starting and ending time in seconds after 0500
SAMPLE INPUT (file milk2.in)

3
300 1000
700 1200
1500 2100

OUTPUT FORMAT

A single line with two integers that represent the longest continuous time of milking and the longest idle time.
SAMPLE OUTPUT (file milk2.out)

900 300
'''
def milk2():
    file=open("milk2.in","r")
    N=int(file.readline().strip())
    period=[]
    for _index in range(N):
        start,end=list(map(int,file.readline().strip().split(" ")))
        period.append([start,end])
    period=sorted(period, key=lambda x:x[0])
    new_period=[period[0]]
    for index in range(1,len(period)):
        if new_period[-1][1]>=period[index][0]:
            new_period[-1][1]=max(new_period[-1][1],period[index][1])
        else:
            new_period.append(period[index])
    res1,res2=0,0
    for index in range(len(new_period)):
        res1=max(res1,new_period[index][1]-new_period[index][0])
        if index>0:
            res2=max(res2,new_period[index][0]-new_period[index-1][1])
    print(res1,res2)
    
milk2()