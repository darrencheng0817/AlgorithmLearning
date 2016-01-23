'''
Created on 1.12.2016

@author: Darren
'''
'''Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
For example,
Given:
s1 = "aabcc",
s2 = "dbbca",n s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
" 
'''
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s3)!=len(s1)+len(s2):
            return False
        dp=[[False]*(len(s2)+1) for _ in range(len(s1)+1)]
        dp[0][0]=True
        for index in range(len(s1)):
            if dp[index][0]==True and s1[index]==s3[index]:
                dp[index+1][0]=True
            else:
                break
        for index in range(len(s2)):
            if dp[0][index]==True and s2[index]==s3[index]:
                dp[0][index+1]=True
            else:
                break
        for index1 in range(1,len(s1)+1):
            for index2 in range(1,len(s2)+1):
                if s1[index1-1]==s3[index1+index2-1] and dp[index1-1][index2]:
                    dp[index1][index2]=True
                if s2[index2-1]==s3[index1+index2-1] and dp[index1][index2-1]:
                    dp[index1][index2]=True
        return dp[-1][-1]

so=Solution()
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
print(so.isInterleave(s1, s2, s3))