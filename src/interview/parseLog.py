'''
Created on 2015.12.1.
input jobname(String)    start/end(boolean)    timeStamp(long)
f1 start 0
f2 start 2
f1 start 5
f1 end 7
f2 end 10
f3 start 11
f3 end 12
f1 end 15
f4 start 16
f4 end 19

// asuming there is only one CPU
// f1: [0,2], [5, 7], [10, 11], [12 15]
// f2: [2,5], [7, 10]. 
// f3: [11, 12]
// f4: [16, 19]

f1 start 0
f1 start 2
f1 start 4
f1 end 6
f1 end 8
f1 end 10
output:log f1 [0,10] 
@author: Darren
'''


N=input()
jobs={}
currentJob=""
res={}
for caseNum in range(N):
    case=input().strip().split(" ")
    jobname=case[0]
    status=case[1]
    timeStamp=int(case[2])
    if status=="start":
        if jobname!=currentJob:
            if currentJob in res:
                currentJob.append()    