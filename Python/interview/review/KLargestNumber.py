'''
Created on 2016年2月29日

@author: Darren
'''
def findKthLargest( nums, k):
    if nums:
        pos = partition(nums, 0, len(nums)-1)
        if k > pos+1:
            return findKthLargest(nums[pos+1:], k-pos-1)
        elif k < pos+1:
            return findKthLargest(nums[:pos], k)
        else:
            return nums[pos]

# choose the right-most element as pivot   
def partition( nums, l, r):
    low = l
    while l < r:
        if nums[l] > nums[r]:
            nums[l], nums[low] = nums[low], nums[l]
            low += 1
        l += 1
    nums[low], nums[r] = nums[r], nums[low]
    return low
nums=[3,1,4,5,6,2,8,7,5]
print(findKthLargest(nums, 3))