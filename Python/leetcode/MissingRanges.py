'''
Created on 1.12.2016

@author: Darren
'''
'''
Given a sorted integer array where the range of elements are [lower, upper] inclusive, return its missing ranges.

For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].
'''
class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """
        if not nums:
            return [str(lower)+"->"+str(upper)] if lower!=upper else [str(lower)]
        if lower!=nums[0]:
            nums=[lower-1]+nums
        if upper!=nums[-1]:
            nums+=[upper+1]
        expected,index=lower,0
        res=[]
        while index<len(nums):
            if nums[index]>expected:
                if nums[index]==nums[index-1]+2:
                    res.append(str(expected))
                else:
                    res.append(str(nums[index-1]+1)+"->"+str(nums[index]-1))
                expected=nums[index]+1
            elif nums[index]==expected:
                expected+=1    
            index+=1
        return res
so=Solution()
nums=[0, 1, 3, 50, 75] 
lower = 0 
upper = 99
print(so.findMissingRanges(nums, lower, upper))
        
                