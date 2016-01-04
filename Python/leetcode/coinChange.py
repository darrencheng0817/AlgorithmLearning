'''
Created on 2016年1月3日

@author: Darren
'''

'''
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

Note:
You may assume that you have an infinite number of each kind of coin.


'''
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp=[amount+1]*(amount+1)
        dp[0]=0
        for i in range(amount):
            for j in range(len(coins)):
                if i+coins[j]>amount:
                    continue
                dp[i+coins[j]]=min(dp[i]+1,dp[i+coins[j]])
        return dp[-1] if dp[-1] <= amount else -1
            
    def coinChange2(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        :BFS solution
        """
        level=0
        queue=[amount]
        visited=set()
        while queue:
            level+=1
            newqueue=[]
            while queue:
                value=queue.pop(0)
                if value in visited:
                    continue
                else:
                    visited.add(value)
                for coin in coins:
                    newValue=value-coin
                    if newValue==0:
                        return level
                    elif newValue>0:
                        newqueue.append(newValue)
            queue=newqueue
        return -1
so=Solution()
print(so.coinChange([413,213,453,20,150,321,254,396,487,234], 5629))
print(so.coinChange2([413,213,453,20,150,321,254,396,487,234], 5629))

