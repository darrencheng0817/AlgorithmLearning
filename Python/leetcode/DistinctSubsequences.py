'''
Created on 1.12.2016

@author: Darren
''''''
from Python.interview.KnightGame import solution
Given a string S and a string T, count the number of distinct subsequences of T in S
A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) 
of the characters without disturbing the relative positions of the remaining characters. 
(ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not)
Here is an example:
S = "rabbbit", T = "rabbit
Return 3.
" 
'''
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if not s:
            return 0
        if not t:
            return 1
        dp=[[0] * (len(t)+1) for _ in  range(len(s)+1)]
        for indexS in range(len(s)): 
            dp[indexS][0]=1
        for indexS in range(len(s)):
            for indexT in range(len(t)):
                if t[indexT]==s[indexS]:
                    dp[indexS+1][indexT+1]=dp[indexS][indexT]+dp[indexS][indexT+1]
                else:
                    dp[indexS+1][indexT+1]=dp[indexS][indexT+1]
        return dp[-1][-1]
s = "rabbbit"
t = "rabbit"
so=Solution()
print(so.numDistinct(s, t))