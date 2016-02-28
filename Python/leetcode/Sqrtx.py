'''
Created on 1.12.2016

@author: Darren
''''''
Implement int sqrt(int x).

Compute and return the square root of x." 
'''
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<0:
            return -1
        if x==0:
            return 0
        l,r=1,x//2+1
        while l<=r:
            m=(l+r)//2
            print(m)
            if x//m>=m and x//(m+1)<(m+1):
                return m
            elif x//m>m:
                l=m+1
            else:
                r=m-1
        return 0
    
so=Solution()
print(so.mySqrt(2))