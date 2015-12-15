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
    
    def bestStrategy(self,nums):
        if not nums:
            return 0
        choseFirst=nums[0]+min(self.bestStrategy(nums[1:-1]),self.bestStrategy(nums[2:]))
        choseLast=nums[-1]+min(self.bestStrategy(nums[:-2]),self.bestStrategy(nums[1:-1]))
        return max(choseLast,choseFirst)                      
    def vsGreddyOp(self,nums):
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        choseFirst=nums[0]
        if nums[1]>=nums[-1]:
            choseFirst+=self.vsGreddyOp(nums[2:])
        else:
            choseFirst+=self.vsGreddyOp(nums[1:-1])
        choseLast=nums[-1]
        if nums[0]>=nums[-2]:
            choseLast+=self.vsGreddyOp(nums[1:-1])
        else:
            choseLast+=self.vsGreddyOp(nums[:-2])
        return max(choseLast,choseFirst)   
nums=[8, 15, 3, 7,5]
so=BestStrategy()
print(so.bestStrategy(nums))
print(so.vsGreddyOp(nums))