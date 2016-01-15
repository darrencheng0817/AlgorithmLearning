'''
Created on 2016年1月11日

@author: Darren
'''
'''
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

'''
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height or len(height)<2:
            return 0
        left,right=0,len(height)-1
        res=0
        while left<right:
            res=max(res,min(height[left],height[right])*(right-left))
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return res