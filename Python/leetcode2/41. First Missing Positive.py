'''
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.
'''
class Solution:
    def firstMissingPositive(self, nums):
        if not nums:
            return 1
        for i, num in enumerate(nums):
            if 0<num<len(nums):
                print(nums, i, num)
                nums[i], nums[num-1] = nums[num-1], nums[i]
        print(nums)
        for i, num in enumerate(nums):
            if num != i+1:
                return i+1
        return len(nums)+1

s = Solution()
print(s.firstMissingPositive([-1,4,2,1,9,10]))