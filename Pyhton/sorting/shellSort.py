'''
Created on 2015.11.30

@author: Darren
'''

def shellSort(nums):
    '''
    Original version
    :type: nums:list[int]
    :rtype: list[int]
    '''
    res = list(nums)
    gap = len(res) // 2
    while gap > 0:
        for i in range(gap):
            for j in range(i + gap, len(res), gap):
                if res[j] < res[j - gap]:
                    temp = res[j]
                    k = j - gap
                    while k >= 0 and res[k] > temp:
                        res[k + gap] = res[k]
                        k -= gap
                    res[k + gap] = temp
        gap //= 2
    return res

def shellSort2(nums):
    '''
    Improved version
    :type: nums:list[int]
    :rtype: list[int]
    '''
    res = list(nums)
    gap = len(res) // 2
    while gap > 0:
        for j in range(gap, len(res)):  # start from gapth element
            if res[j] < res[j - gap]:  # insertion sort 
                temp = res[j]
                k = j - gap
                while k >= 0 and res[k] > temp:
                    res[k + gap] = res[k]
                    k -= gap
                res[k + gap] = temp
        gap //= 2
    return res
def shellSort3(nums):
    '''
    Advanced version
    :type: nums:list[int]
    :rtype: list[int]
    '''
    res = list(nums)
    gap = len(res) // 2
    while gap > 0:
        for j in range(gap, len(res)):  # start from gapth element
            if res[j] < res[j - gap]:  # insertion sort, use swap instead of shift 
                k = j - gap
                while k >= 0 and res[k] > res[k + gap]:
                    res[k], res[k + gap] = res[k + gap], res[k]
                    k -= gap
        gap //= 2
    return res
nums = [1, 9, 5, 4, 3, 1, 3, 4, 5, 6, 2, 3]
print(shellSort(nums))
print(shellSort2(nums))
print(shellSort3(nums))
