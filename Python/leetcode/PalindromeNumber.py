'''
Created on 1.12.2016

@author: Darren
''''''
Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

Some hints:

Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.

" 
'''
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        head=1
        while head*10<=x:
            head*=10
        while x>0:
            if x//head!=x%10:
                return False
            x%=head
            head//=100
            x//=10
        return True
        
so=Solution()
print(so.isPalindrome(1235321))
