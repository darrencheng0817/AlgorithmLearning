'''
Created on 2015年12月11日
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
@author: Darren
'''
'''
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
'''
def bestTime(prices):
    if not prices:
        return 0
    maxProfit_l=0
    maxProfit=0
    for index in range(1,len(prices)):
        maxProfit_l=max(maxProfit_l+prices[index]-prices[index-1],0)
        maxProfit=max(maxProfit,maxProfit_l)
    return maxProfit

'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). 
However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''
def bestTime2(prices):
    res=0
    for index in range(1,len(prices)):
        if prices[index]-prices[index-1]>0:
            res+=prices[index]-prices[index-1]
    return res

'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''
'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
'''
def bestTime3(prices,k):
    if not prices:
        return 0
    localDP=[0]*(k+1)
    globalDP=[0]*(k+1)
    for i in range(1,len(prices)):
        diff=prices[i]-prices[i-1]
        for j in range(k,0,-1):
            localDP[j]=max(globalDP[j-1]+diff,localDP[j]+diff)
            globalDP[j]=max(globalDP[j],localDP[j])
    return globalDP[-1]
print(bestTime3([2,1,2,0,1],2))

'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

prices = [1, 2, 3, 0, 2]
maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]
'''
def bestTime4(prices):
    if not prices:
        return 0
    sell=[0]*len(prices)
    buy=[0]*len(prices)
    buy[0]=-prices[0]
    for dayIndex in range(1,len(prices)):
        sell[dayIndex]=max(buy[dayIndex-1]+prices[dayIndex],sell[dayIndex-1])
        if dayIndex>2:
            buy[dayIndex]=max(sell[dayIndex-2]-prices[dayIndex],buy[dayIndex-1])
        else:
            buy[dayIndex]=max(-prices[dayIndex],buy[dayIndex-1])
    return sell[-1]

def bestTime5(prices):
    if not prices:
        return 0
    sell, buy, prev_sell, prev_buy = 0, -prices[0], 0, 0
    for price in prices:
        prev_buy = buy
        buy = max(prev_sell - price, prev_buy)
        prev_sell = sell
        sell = max(prev_buy + price, prev_sell)
    return sell 
print(bestTime4([1, 2, 4]))