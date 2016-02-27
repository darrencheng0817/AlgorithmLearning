'''
Created on 1.12.2016

@author: Darren
''''''
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...



1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.



Given an integer n, generate the nth sequence.



Note: The sequence of integers will be represented as a string.

" 
'''
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res="1"
        for _ in range(n-1):
            num,count=res[0],1
            new_res=""
            for index in range(1,len(res)):
                if res[index]==num:
                    count+=1
                else:
                    new_res+=(str(count)+num)
                    num=res[index]
                    count=1
            new_res+=(str(count)+num)
            res=new_res
        return res
            
        
so=Solution()
print(so.countAndSay(6))