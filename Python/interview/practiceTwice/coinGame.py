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
        pass
    
    def vsGreddyOp(self,nums):
        pass
nums=[8, 15, 3, 7,5]
so=BestStrategy()
print(so.bestStrategy(nums))
print(so.vsGreddyOp(nums))