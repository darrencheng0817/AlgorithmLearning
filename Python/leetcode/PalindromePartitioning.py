'''
Created on 1.12.2016

@author: Darren
''''''

Given a string s, partition s such that every substring of the partition is a palindrome.


Return all possible palindrome partitioning of s.


For example, given s = "aab",

Return

  [
    ["aa","b"],
    ["a","a","b"]
  ]

" 
'''
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res=[]
        def util(start,item):
            if start==len(s):
                res.append(item)
                return
            for index in range(start+1,len(s)+1):
                if s[start:index]==s[start:index][::-1]:
                    util(index,item+[s[start:index]])
        util(0,[])
        return res
so=Solution()
print(so.partition("aab"))