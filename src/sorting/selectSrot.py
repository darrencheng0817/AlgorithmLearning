'''
Created on 2015.11.30

@author: Darren
'''

def selectSort(nums):
    """
    Original version
    :type nums:list[int] numRange:int
    :rtype list[int]
    """
    res = list(nums)
    for i in range(len(res)):
        minIndex = i
        for j in range(i + 1, len(res)):
            if res[j] < res[minIndex]:
                minIndex = j
        res[i], res[minIndex] = res[minIndex], res[i]
    return res


nums = [1,9, 5, 4, 3, 1, 3, 4, 5, 6, 2, 3]
print(selectSort(nums))