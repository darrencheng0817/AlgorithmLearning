'''
Created on 1.12.2016

@author: Darren
''''''
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list." 
'''
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry=1
        for i in range(len(digits)-1,-1,-1):
            temp=digits[i]+carry
            digits[i]=temp%10
            if temp>=10:
                carry=1
            else:
                carry=0
                break
        return digits if carry==0 else [1]+digits