'''
Created on 1.12.2016

@author: Darren
''''''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:
"((()))", "(()())", "(())()", "()(())", "()()()"
" 
'''
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res=[]
        self.generateParenthesisUtil(n,n,res,"")
        return res
        
    def generateParenthesisUtil(self,left,right,res,item):
        if right==0:
            res.append(item)
            return
        if left>0:
            self.generateParenthesisUtil(left-1,right,res,item+"(")
        if right>left:
            self.generateParenthesisUtil(left,right-1,res,item+")")