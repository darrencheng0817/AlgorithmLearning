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
    if not nums:
        return 
    slow,fast=nums[0],nums[0]
    while True:
        fast=nums[nums[fast]]
        slow=nums[slow]
        if fast==slow:
            break
    slow=nums[0]
    while slow!=fast:
        fast=nums[fast]
        slow=nums[slow]
    return slow    
print(findDuplicate([1,2,3,4,5,6,6,7]))