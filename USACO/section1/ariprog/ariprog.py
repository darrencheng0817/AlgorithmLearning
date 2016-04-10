'''
Created on 2016年3月2日

@author: Darren
'''
'''
Arithmetic Progressions
An arithmetic progression is a sequence of the form a, a+b, a+2b, ..., a+nb where n=0,1,2,3,... . For this problem, a is a non-negative integer and b is a positive integer.

Write a program that finds all arithmetic progressions of length n in the set S of bisquares. The set of bisquares is defined as the set of all integers of the form p2 + q2 (where p and q are non-negative integers).

TIME LIMIT: 5 secs

PROGRAM NAME: ariprog

INPUT FORMAT

Line 1:    N (3 <= N <= 25), the length of progressions for which to search
Line 2:    M (1 <= M <= 250), an upper bound to limit the search to the bisquares with 0 <= p,q <= M.
SAMPLE INPUT (file ariprog.in)

5
7
OUTPUT FORMAT

If no sequence is found, a single line reading `NONE'. Otherwise, output one or more lines, each with two integers: the first element in a found sequence and the difference between consecutive elements in the same sequence. The lines should be ordered with smallest-difference sequences first and smallest starting number within those sequences first.

There will be no more than 10,000 sequences.

SAMPLE OUTPUT (file ariprog.out)

1 4
37 4
2 8
29 8
1 12
5 12
13 12
17 12
5 20
2 24
'''
import time
def airgrog(N,M):
    bisquares=set()
    max_bis=0
    for i in range(M+1):
        for j in range(i,M+1):
            bis=i*i+j*j
            max_bis=max(max_bis,bis)
            bisquares.add(bis)
    res=[]
    for b in range(1,max_bis//(N-1)+1):        
        for a in range(max_bis-N):
            if a+b*(N-1)>max_bis:
                break
            isOk=True
            for i in range(N):
                if a+i*b not in bisquares:
                    isOk=False
                    break
            if isOk:
                res.append((a,b))
    return res
        
start=time.clock()
print(airgrog(18, 100))
end=time.clock()
print(end-start)    
