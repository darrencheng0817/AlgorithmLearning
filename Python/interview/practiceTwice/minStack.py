'''
Created on 2015年12月1日
https://leetcode.com/problems/min-stack/
@author: Darren
'''
class MinStack(object):
    def __init__(self):
        pass
    
    def pop(self):
        pass
    
    def push(self,num):
        pass
             
    def getMin(self):
        pass

minstack=MinStack()
minstack.push(0)
nums=[1,3,4,5,2,3,1]
for num in nums:
    minstack.push(num)
    minstack.pop()
    print(minstack.getMin())