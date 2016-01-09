'''
Created on 2016年1月8日

@author: Darren
'''
'''
Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?

'''
def isPowerOfThree(n):
    """
    :type n: int
    :rtype: bool
    """
    return n > 0 and 3**19 % n==0

print(isPowerOfThree(27))