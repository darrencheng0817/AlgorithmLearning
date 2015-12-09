'''
Created on 2015年12月8日
Problem statement: Consider a row of n coins of values v1 . . . vn, 
where n is even. We play a game against an opponent by alternating turns. 
In each turn, a player selects either the first or last coin from the row, 
removes it from the row permanently, and receives the value of the coin. 
Determine the maximum possible amount of money we can definitely win if we move first.

Note: The opponent is as clever as the user.
@author: Darren
'''


class BestStrategy(object):
    def __init__(self):
        self.selection=[]
    def bestStrategy(self,nums):
        if not nums:
            return 0
        resFirst=nums[0]+min(self.bestStrategy(nums[1:-1]),self.bestStrategy(nums[2:]))
        resLast=nums[-1]+min(self.bestStrategy(nums[:-2]),self.bestStrategy(nums[1:-1]))    
        return max(resFirst,resLast)
    
    def vsGreddyOp(self,nums):
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        resFirst,resLast=0,0
        if nums[1]>=nums[-1]:
            resFirst=nums[0]+self.vsGreddyOp(nums[2:])
        else:
            resFirst=nums[0]+self.vsGreddyOp(nums[1:-1])
        if nums[0]>=nums[-2]:
            resLast=nums[-1]+self.vsGreddyOp(nums[1:-1])
        else:
            resLast=nums[-1]+self.vsGreddyOp(nums[0:-2])
        return max(resFirst,resLast)
nums=[8, 15, 3, 7,5]
so=BestStrategy()
print(so.bestStrategy(nums))
print(so.vsGreddyOp(nums))