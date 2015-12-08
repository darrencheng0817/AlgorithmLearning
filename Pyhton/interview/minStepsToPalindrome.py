'''
Created on 2015年12月1日
给一个字符串，问最少删去多少个字符可以得到一个是回文的字符串, 只能删去头尾处的字符 eg "abxyyxc" -> 3
@author: Darren
'''

def longestPalindromeSubstring(string):
    if not string:
        return ""
    res=""
    for i in range(len(string)):
        length=1
        while i-length>=0 and i+length<len(string) and string[i-length]==string[i+length]:
            length+=1
        if length*2-1>len(res):
            res=string[i-length+1:i+length]    
        length=1
        while i-length>=0 and i+length+1<len(string) and string[i-length]==string[i+length+1]:
            length+=1
        if length*2>len(res):
            res=string[i-length+1:i+length+1]   
    return res
def minDeletion2Palindrome(string):
    longestPalindrom=longestPalindromeSubstring(string)
    return len(string)-len(longestPalindrom)

def longestPalindromeSubSeq(string):
    if not string:
        return ""
    dp=[[1]*len(string) for i in range(len(string))]
    for length in range(2,len(string)+1):
        for i in range(len(string)-length+1):
            j=i+length-1
            if length==2 and string[i]==string[j]:
                dp[i][j]=2
            elif string[i]==string[j]:
                dp[i][j]=dp[i+1][j-1]+2
            else:
                dp[i][j]=max(dp[i][j-1],dp[i+1][j])
    return dp[0][-1]           
print(minDeletion2Palindrome("abxyyxbc"))
print(longestPalindromeSubSeq("akfdshda"))