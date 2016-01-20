'''
Created on 1.12.2016

@author: Darren
''''''
Given a string containing just the characters  (  and  ) , find the length of the longest valid (well-formed) parentheses substring.
For "(()", the longest valid parentheses substring is "()", which has length = 2.
Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
" 
'''
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        stack=[]
        start,res=0,0
        for index,char in enumerate(s):
            if char=="(":
                stack.append(index)
            else:
                if not stack:
                    start=index+1
                else:
                    stack.pop()
                    if stack:
                        res=max(res,index-stack[-1])
                    else:
                        res=max(res,index-start+1)
        return res