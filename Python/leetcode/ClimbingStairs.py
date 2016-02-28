'''
Created on 1.12.2016

@author: Darren
''''''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
" 
'''
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=0:
            return 0
        if n==1:
            return 1
        count1=1
        count2=2
        for _ in range(2,n):
            temp=count2
            count2+=count1
            count1=temp
        return count2