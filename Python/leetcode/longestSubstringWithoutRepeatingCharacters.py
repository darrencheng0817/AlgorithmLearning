'''
Created on 2016年1月9日

@author: Darren
'''
'''
Given a string, find the length of the longest substring without repeating characters. 
For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. 
For "bbbbb" the longest substring is "b", with the length of 1.
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        d={}
        res,localSum=0,0
        for index in range(len(s)):
            if s[index] not in d:
                localSum+=1
                d[s[index]]=index
            else:
                res=max(res,localSum)
                startIndex=index-localSum
                while s[startIndex]!=s[index]:
                    d.pop(s[startIndex])
                    startIndex+=1
                localSum=index-startIndex
            index+=1
        res=max(res,localSum)
        return res

    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        res,local_count=0,0
        d={}
        for index,char in enumerate(s):
            if char not in d:
                d[char]=index
                local_count+=1
            else:
                res=max(res,local_count)
                start_index=index-local_count
                while s[start_index]!=char:
                    d.pop(s[start_index])
                    start_index+=1
                local_count=index-start_index
                d[char]=index
        res=max(res,local_count)
        return res
so=Solution()
s="aabcvfgrgb"
print(so.lengthOfLongestSubstring(s))
print(so.lengthOfLongestSubstring2(s))