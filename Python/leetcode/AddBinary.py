'''
Created on 1.12.2016

@author: Darren
'''
'''
Given two binary strings, return their sum (also a binary string).
For example,
a = "11"
b = "1"
Return "100".
" 
'''
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry=0
        res=""
        for index in range(max(len(a),len(b))):
            da,db=0,0
            if len(a)-index-1>=0:
                da=int(a[len(a)-index-1])
            if len(b)-index-1>=0:
                db=int(b[len(b)-index-1])
            sum_d=da+db+carry
            carry=sum_d//2
            res=str(sum_d%2)+res
        if carry==1:
            res="1"+res
        return res