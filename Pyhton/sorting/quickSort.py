'''
Created on 2015.11.30

@author: Darren
'''

def quickSrotUtil(nums, l, r):
    if l<r:
        i, j, x = l, r, nums[l]
        while i < j:
            while i < j and nums[j] >= x:
                j -= 1
            if i < j:
                nums[i] = nums[j]
                i += 1
            while i < j and nums[i] < x:
                i += 1
            if i < j:
                nums[j] = nums[i]
                j-=1
        nums[i] = x
        quickSrotUtil(nums, l, i - 1)
        quickSrotUtil(nums, i + 1, r)

def quickSort(nums):
    """
    Original version
    :type nums:list[int] numRange:int
    :rtype list[int]
    """
    res = list(nums)
    quickSrotUtil(res,0,len(res)-1)
    return res

nums = [1,9, 5, 4, 3, 1, 3, 4, 5, 6, 2, 3]
print(quickSort(nums))