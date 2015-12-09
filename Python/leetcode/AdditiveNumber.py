# Additive number is a string whose digits can form additive sequence.
# 
# A valid additive sequence should contain at least three numbers. Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.
# 
# For example:
# "112358" is an additive number because the digits can form an additive sequence: 1, 1, 2, 3, 5, 8.
# 
# 1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
# "199100199" is also an additive number, the additive sequence is: 1, 99, 100, 199.
# 1 + 99 = 100, 99 + 100 = 199
# Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.
# 
# Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.
# 
# Follow up:
# How would you handle overflow for very large input integers?




class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if len(num)< 2:
            return False
        first,second=0,0
        for i in range(1,len(num)-1):
            if num[0]=='0' and i>1:
                break
            for j in range(i+1,len(num)):
                if num[i]=='0' and j>i+1:
                    break
                first=int(num[0:i])
                second=int(num[i:j])
                k=j
                while k<len(num):
                    result=str(first+second)
                    if num[k:].startswith(result):
                        first,second=second,int(result)
                        k+=len(result)
                    else:
                        break
                    if k==len(num):
                        return True
        return False
                        
                    
        
so=Solution()
num="000"
print(so.isAdditiveNumber(num))