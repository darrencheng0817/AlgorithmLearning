'''
Created on 1.12.2016

@author: Darren
''''''
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:

00 - 0
01 - 1
11 - 3
10 - 2


Note:
For a given n, a gray code sequence is not uniquely defined.

For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.

For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that." 
'''
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n==0:
            return [0]
        grays=["0","1"]
        for _ in range(1,n):
            first_part=["0"+item for item in grays]
            second_part=["1"+item for item in reversed(grays)]
            grays=first_part+second_part
        res=[]
        for item in grays:
            res.append(int(item,2))
        return res
        
so=Solution()
print(so.grayCode(0))