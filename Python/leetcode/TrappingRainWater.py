'''
Created on 1.12.2016

@author: Darren
''''''

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining. 



For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.




The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!" 
'''
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l,r=0,len(height)-1
        res=0
        while l<r:
            min_height=min(height[l],height[r])
            if min_height==height[l]:
                l+=1
                while l<r and height[l]<min_height:
                    res+=min_height-height[l]
                    l+=1
            else:
                r-=1
                while l<r and height[r]<min_height:
                    res+=min_height-height[r]
                    r-=1
        return res