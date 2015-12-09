'''
Created on 2015年12月1日
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
https://leetcode.com/problems/trapping-rain-water/
@author: Darren
'''

def tarppingRainWater(nums):
    l,r=0,len(nums)-1
    res=0
    while l<r:
        minNum=min(nums[l],nums[r])
        if minNum==nums[l]:
            l+=1
            while l<r and nums[l]<minNum:
                res+=minNum-nums[l]
                l+=1
        else:
            r-=1
            while l<r and nums[r]<minNum:
                res+=minNum-nums[r]
                r-=1
    return res

nums=[0,1,0,2,1,0,1,3,2,1,2,1]
print(tarppingRainWater(nums ))