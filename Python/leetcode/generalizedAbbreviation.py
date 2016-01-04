'''
Created on 2016年1月3日

@author: Darren
'''
'''
Write a function to generate the generalized abbreviations of a word.

Example:
Given word = "word", return the following list (order does not matter):
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
'''
class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        return [word] + [word[:first] + str(last - first + 1) + word[last+1:last+2] + rest
                     for last in range(len(word))
                     for first in range(last + 1)
                     for rest in self.generateAbbreviations(word[last+2:])]


so=Solution()
print(so.generateAbbreviations("word"))