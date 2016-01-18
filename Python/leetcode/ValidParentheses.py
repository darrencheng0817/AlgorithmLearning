'''
Created on 1.12.2016

@author: Darren
''''''
Given a string containing just the characters  ( ,  ) ,  { ,  } ,  [  and  ] , determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
" 
'''
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        dic={")":"(","}":"{","]":"["}
        stack=[]
        for char in s:
            if char in ["{","[","("]:
                stack.append(char)
            else:
                if not stack or dic[char]!=stack.pop():
                    return False
        return not stack