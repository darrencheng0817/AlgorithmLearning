'''
Created on 2015.11.30

@author: Darren
'''

def insertionSort(nums):
    """
    Original version
    :type nums:list[int]
    :rtype list[int]
    """
    res=list(nums)
    for i in range(1,len(res)):
        #find a place for res[i]
        j=i-1
        while j>=0:
            if res[i]>res[j]:
                break
            j-=1
        #if we get one
        if j!=i-1:
            #move element that large than res[i] forward    
            temp=res[i]
            for k in range(i,j,-1):
                res[k]=res[k-1]
            res[j+1]=temp
    return res

def insertionSort2(nums):
    """
    Improved version,merged the find and move forward step
    :type nums:list[int]
    :rtype list[int]
    """
    res=list(nums)
    for i in range(1,len(res)):
        #if res[i]>=res[i-1] res[:0] are already sorted
        if res[i]<res[i-1]:
            temp=res[i]
            j=i-1
            while j>=0 and res[j]>temp:
                res[j+1]=res[j]
                j-=1
            res[j+1]=temp
    return res

def insertionSort3(nums):
    """
    Advanced version,merged the find and move forward step, replace move with swap
    :type nums:list[int]
    :rtype list[int]
    """
    res=list(nums)
    for i in range(1,len(res)):
        #if res[i]>=res[i-1] res[:0] are already sorted
        if res[i]<res[i-1]:
            j=i-1
            while j>=0 and res[j]>res[j+1]:
                res[j+1],res[j]=res[j],res[j+1]
                j-=1
    return res


nums = [1,9, 5, 4, 3, 1, 3, 4, 5, 6, 2, 3]
print(insertionSort(nums))
print(insertionSort2(nums))
print(insertionSort3(nums))