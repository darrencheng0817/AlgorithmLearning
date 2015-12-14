'''
Created on 2015年12月1日
给一个字符串，问最少删去多少个字符可以得到一个是回文的字符串, 只能删去头尾处的字符 eg "abxyyxc" -> 3
@author: Darren
'''

def longestPalindromeSubstring(string):
    pass 

def minDeletion2Palindrome(string):
    longestPalindrom=longestPalindromeSubstring(string)
    return len(string)-len(longestPalindrom)

def longestPalindromeSubSeq(string):
    pass         
print(minDeletion2Palindrome("abxyyxbc"))
print(longestPalindromeSubSeq("akfdshda"))