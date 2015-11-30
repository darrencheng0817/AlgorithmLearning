'''
Created on 2015年11月30日

@author: Darren
'''
def countingSort(nums,numRange):
    """
    Original version
    :type nums:list[int] numRange:int
    :rtype list[int]
    """
    l=[0]*numRange
    for num in nums:
        l[num]+=1
    for i in range(1,numRange):
        l[i]+=l[i-1]
    res=[0]*len(nums)
    for num in reversed(nums): #loop from back to front to ensure the original order
        res[l[num]-1]=num
        l[num]-=1
    return res

nums=[12,14,2,4,1,0,3,34,23,53,53,90,7,5,4,3,25,45,5,46]
print(countingSort(nums,100))