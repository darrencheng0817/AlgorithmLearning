'''
Created on 2016年2月27日

@author: Darren
'''
'''
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:
For the return value, each inner list's elements must follow the lexicographic order.
All inputs will be in lower-case.
'''
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d={}
        for string in strs:
            sorted_s="".join(sorted(string))
            if sorted_s not in d:
                d[sorted_s]=[]
            d[sorted_s].append(string)
        res=[]
        for key in d.keys():
            res.append(sorted(d[key]))
        return res