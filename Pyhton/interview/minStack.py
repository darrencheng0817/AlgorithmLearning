'''
Created on 2015年12月1日
https://leetcode.com/problems/min-stack/
@author: Darren
'''
class MinStack(object):
    def __init__(self):
        self.stack=[]
        self.minStack=[]
    
    def pop(self):
        if not self.stack:
            raise Exception("Stack is Empty!")
        num=self.stack.pop()
        if num==self.minStack[-1]:
            self.minStack.pop()
        return num
    
    def push(self,num):
        self.stack.append(num)
        if self.minStack:
            if num<=self.minStack[-1]:
                self.minStack.append(num)
        else:
            self.minStack.append(num)  
             
    def getMin(self):
        if self.minStack:
            return self.minStack[-1]
        else:
            raise Exception("Stack is Empty!")

minstack=MinStack()
minstack.push(0)
nums=[1,3,4,5,2,3,1]
for num in nums:
    minstack.push(num)
    minstack.pop()
    print(minstack.getMin())