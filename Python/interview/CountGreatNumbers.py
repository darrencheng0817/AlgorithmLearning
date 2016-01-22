'''
Created on 2016年1月21日

@author: Darren
'''
def countGreater(nums):
    def sort(enum):
        half = len(enum) // 2
        if half:
            left, right = sort(enum[:half]), sort(enum[half:])
            for i in range(len(enum))[::-1]:
                if not right or left and left[-1][1] < right[-1][1]:
                    smaller[left[-1][0]] += len(right)
                    enum[i] = left.pop()
                else:
                    enum[i] = right.pop()
        return enum
    smaller = [0] * len(nums)
    sort(list(enumerate(nums)))
    return smaller

# Complete the function below.

def  countGreaterNumbers( a,  b):
    d={}
    for num in a:
        if num not in d:
            d[num]=0
        d[num]+=1
    sortedKey=sorted(d.keys(),reverse=True)
    print(d)
    print(sortedKey)
    preValue=0
    for index in range(len(sortedKey)):
        temp=d[sortedKey[index]]
        if index==0:
            d[sortedKey[index]]=0
        else:
            d[sortedKey[index]]=d[sortedKey[index-1]]+preValue
        preValue=temp
    print(d)
    res=[]
    for num in b:
        res.append(d[a[num-1]])
    return res

a=[3,4,1,2,4,6]
b=[1,2,3,4,5,6]
print(countGreaterNumbers(a,b))