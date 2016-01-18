'''
Created on 2016年1月17日

@author: Darren
'''
def  countUneatenLeaves( N,  A):
    res=0
    count=[1]*len(A)
    nextNum=0
    while True:
        nextNum=min([count[index]*j for index,j in enumerate(A)])
        if nextNum>N:
            break
        for index,j in enumerate(A):
            if nextNum==count[index]*j:
                count[index]+=1
        res+=1
    return N-res
print(countUneatenLeaves(10, [2, 4,5]))