'''
Created on 2016年1月11日

@author: Darren
'''
'''
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

'''
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        dicts=["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        res=[""]
        for digit in digits:
            newRes=[pre+newChar for pre in res for newChar in dicts[int(digit)-2]]
            res=newRes
        return res
        
so=Solution()
digits="23"
print(so.letterCombinations(digits))