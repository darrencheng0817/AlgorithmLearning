'''
Created on 1.12.2016

@author: Darren
''''''

A message containing letters from A-Z is being encoded to numbers using the following mapping:



 A  -> 1
 B  -> 2
...
 Z  -> 26



Given an encoded message containing digits, determine the total number of ways to decode it.



For example,
Given encoded message "12",
it could be decoded as "AB" (1 2) or "L" (12).



The number of ways decoding "12" is 2.
" 
'''
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        dp=[0]*(len(s)+1)
        dp[0]=1
        for index,char in enumerate(s):
            if 0<int(char)<=9:
                dp[index+1]+=dp[index]
            if index>0 and 10<=int(s[index-1:index+1])<=26:
                dp[index+1]+=dp[index-1]
        return dp[-1]
                