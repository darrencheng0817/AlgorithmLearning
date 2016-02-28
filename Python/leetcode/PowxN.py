'''
Created on 1.12.2016

@author: Darren
''''''
Implement pow(x, n).
" 
'''
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:
            return 1.0
        elif n<0:
            return 1/self.myPow(x,-n)
        else:
            v=self.myPow(x,n//2)
            if n&1==1:
                return v*v*x
            else:
                return v*v