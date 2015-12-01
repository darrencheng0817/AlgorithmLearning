'''
Created on 2015.11.30

@author: Darren
'''

def merge(a,b):
    indexA,indexB=0,0
    res=[]
    while indexA<len(a) and indexB<len(b):
        if a[indexA]>b[indexB]:
            res.append(b[indexB])
            indexB+=1
        else:
            res.append(a[indexA])
            indexA+=1
    for i in range(indexA,len(a)):
        res.append(a[i])
    for i in range(indexB,len(b)):
        res.append(b[i])   
    return res

def mergeSort(nums):
    """
    Original version
    :type nums:list[int] numRange:int
    :rtype list[int]
    """
    if len(nums)<=1:
        return nums
    mid=len(nums)//2
    return merge(mergeSort(nums[:mid]),mergeSort(nums[mid:]))
    
nums = [1,9, 5, 4, 3, 1, 3, 4, 5, 6, 2, 3]
print(mergeSort(nums))