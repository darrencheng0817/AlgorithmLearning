'''
Created on 1.12.2016

@author: Darren
''''''

Given n non-negative integers representing the histogram s bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.




Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].




The largest rectangle is shown in the shaded area, which has area = 10 unit.



For example,
Given height = [2,1,5,6,2,3],
return 10.
" 
'''
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        stack=[]
        res=0
        for cur_index,height in enumerate(heights):
            while stack and height<heights[stack[-1]]:
                index=stack.pop()
                local_res=0
                if stack:
                    local_res=heights[index]*(cur_index-stack[-1]-1)
                else:
                    local_res=heights[index]*(cur_index)
                res=max(res,local_res)
            stack.append(cur_index)
        while stack:
            index=stack.pop()
            local_res=0
            if stack:
                local_res=heights[index]*(len(heights)-stack[-1]-1)
            else:
                local_res=heights[index]*len(heights)
            res=max(res,local_res)
        return res
            