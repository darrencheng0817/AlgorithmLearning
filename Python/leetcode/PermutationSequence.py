'''
Created on 1.12.2016

@author: Darren
''''''
The set [1,2,3,&#8230;,n] contains a total of n! unique permutation
By listing and labeling all of the permutations in order,
We get the following sequence (ie, for n = 3):
"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.
Note: Given n will be between 1 and 9 inclusive." 
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
def getPermutation(M,N):
    M-=1
    res=[]
    factorial=1
    nums=list(range(1,N+1))
    for roundCount in range(2,N):
        factorial*=roundCount
    roundCount=N-1
    while roundCount>=0:
        index=M//factorial
        M%=factorial
        res.append(nums[index])
        nums.pop(index)
        if roundCount>0:
            factorial//=roundCount
        roundCount-=1
    return " ".join(str(_) for _ in res)
      
inputString=input().strip().split(" ")
M=int(inputString[0])
N=int(inputString[1])
print(getPermutation(M,N))