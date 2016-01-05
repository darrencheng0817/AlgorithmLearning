'''
Created on 2016年1月4日

@author: Darren
'''
'''
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:
Given ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
Return 16
The two words can be "abcw", "xtfn".

Example 2:
Given ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
Return 4
The two words can be "ab", "cd".

Example 3:
Given ["a", "aa", "aaa", "aaaa"]
Return 0
No such pair of words.
'''
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        d={}
        for word in words:
            wordSet=set(word)
            key=''.join(sorted(list(wordSet)))
            if key in d:
                if len(word)>d[key]:
                    d[key]=len(word)
            else:
                d[key]=len(word)
        res=0
        keyList=list(d.keys())
        for i in range(len(keyList)):
            for j in range(i+1,len(keyList)):
                set1,set2=set(keyList[i]),set(keyList[j])
                if not (set1&set2):
                    res=max(res,d[keyList[i]]*d[keyList[j]])
        return res

so=Solution()
words=["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
print(so.maxProduct(words))
                