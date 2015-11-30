'''
Created on 2015.11.29
Bubble Sort
@author: Darren
'''


def bubbleSort(nums):
    """
    Original version
    :type nums: List[int]
    :rtype: List[int]
    """
    res = list(nums)  # I don't want to change the input list
    for i in range(len(res)):
        for j in range(1, len(res)):
            if res[j - 1] > res[j]:
                res[j - 1], res[j] = res[j], res[j - 1]
    return res

def bubbleSort2(nums):
    """
    Improved version, stop when no swap occur
    :type nums: List[int]
    :rtype: List[int]
    """
    res = list(nums)  # I don't want to change the input list
    flag = True
    while flag:
        flag = False
        for j in range(1, len(res)):
            if res[j - 1] > res[j]:
                res[j - 1], res[j] = res[j], res[j - 1]
                flag = True
    return res

def bubbleSort3(nums):
    """
    Advanced version, cache the index of swaped element and stop at this index
    in the next loop, because the elements behind that are already sorted 
    :type nums: List[int]
    :rtype: List[int]
    """
    res = list(nums)  # I don't want to change the input list
    flag = len(res)
    while flag > 0:
        k = flag
        flag = 0
        for j in range(1, k):
            if res[j - 1] > res[j]:
                res[j - 1], res[j] = res[j], res[j - 1]
                flag = j
    return res
nums = [9, 5, 4, 3, 1, 3, 4, 5, 6, 2, 3]
print(bubbleSort(nums))
print(bubbleSort2(nums))
print(bubbleSort3(nums))
