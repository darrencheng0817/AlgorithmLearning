'''
Created on 1.12.2016

@author: Darren
''''''
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?
Would this affect the run-time complexity? How and why?
Write a function to determine if a given target is in the array." 
'''
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return 0
        l,r=0,len(nums)-1
        while l<=r:
            m=(l+r)//2
            if nums[m]==target:
                return True
            elif nums[m]>nums[l]:
                if nums[m]>target and target>=nums[l]:
                    r=m-1
                else:
                    l=m+1
            elif nums[m]<nums[l]:
                if nums[m]<target and target<=nums[r]:
                    l=m+1
                else:
                    r=m-1
            else:
                l+=1
        return False