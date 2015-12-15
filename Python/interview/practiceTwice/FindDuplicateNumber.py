'''
Created on 2015年12月6日
https://leetcode.com/problems/find-the-duplicate-number/
@author: Darren
'''
def findDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    slow,fast=nums[0],nums[0]
    while True:
        fast=nums[nums[fast]]
        slow=nums[slow]
        if fast==slow:
            break
    fast=nums[0]
    while fast!=slow:
        fast=nums[fast]
        slow=nums[slow]
    return slow
print(findDuplicate([1,2,3,4,5,6,6,7]))