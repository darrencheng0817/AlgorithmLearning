'''
Created on 2016年4月21日

@author: Darren
'''
'''
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?
'''
def isPowerOfFour(num):
    """
    :type num: int
    :rtype: bool
    """
    return num > 0 and (num&(num-1)) == 0 and (num & 0x55555555) != 0

print(isPowerOfFour(64))