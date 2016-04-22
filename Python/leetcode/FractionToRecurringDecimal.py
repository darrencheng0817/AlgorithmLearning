'''
Created on 1.12.2016

@author: Darren
''''''
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".



Credits:Special thanks to @Shangrila for adding this problem and creating all test cases." 
'''
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator==0:
            return "0"
        if denominator==0:
            raise Exception()
        res=""
        if numerator*denominator<0:
            res="-"
        if numerator<0 or denominator<0:
            numerator=abs(numerator)
            denominator=abs(denominator)

        res+=str(numerator//denominator)
        rest=numerator%denominator
        if rest==0:
            return res
        res+="."
        repeat={}
        while rest>0:
            rest*=10
            if rest in repeat:
                res=res[:repeat[rest]-1]+"("+res[repeat[rest]-1:]+")"
                break
            res+=str(rest//denominator)
            repeat[rest]=len(res)
            rest=rest%denominator
        return res
so=Solution()
print(so.fractionToDecimal(-1,-2147483648))