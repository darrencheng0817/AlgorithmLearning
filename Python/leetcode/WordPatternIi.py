'''
Created on 1.12.2016

@author: Darren
'''
'''
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty substring in str.

Examples:
pattern = "abab", str = "redblueredblue" should return true.
pattern = "aaaa", str = "asdasdasdasd" should return true.
pattern = "aabb", str = "xyzabcxzyabc" should return false.
Notes:
You may assume both pattern and str contains only lowercase letters.

'''
class Solution(object):
    def wordPatternMatch(self, pattern, string):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        d={}
        def util(pattern,string):
            if not pattern and not string:
                return True
            elif pattern and string:
                for end in range(1,len(string)+1):
                    if pattern[0] not in d and string[:end] not in d.values():
                        d[pattern[0]]=string[:end]
                        if util(pattern[1:],string[end:]):
                            return True
                        d.pop(pattern[0])
                    elif pattern[0] in d and d[pattern[0]]==string[:end]:
                        if util(pattern[1:],string[end:]):
                            return True
            return False
        return util(pattern,string)
        
so=Solution()
pattern = "abab"
string = "redblueredblue"
print(so.wordPatternMatch(pattern, string))