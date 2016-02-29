'''
Created on 1.12.2016

@author: Darren
''''''
from leetcode.BinaryTreeMaximumPathSum import Solution

Implement the following operations of a stack using queues.


push(x) -- Push element x onto stack.


pop() -- Removes the element on top of the stack.


top() -- Get the top element.


empty() -- Return whether the stack is empty.


Notes:

You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).




Update (2015-06-11):
The class name of the Java function had been updated to MyStack instead of Stack.


Credits:Special thanks to @jianchao.li.fighter for adding this problem and all test cases." 
'''
class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q1=[]
        self.q2=[]
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.q1.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        while self.q1:
            self.q2.append(self.q1.pop(0))
        self.q2.pop()
        while self.q2:
            self.q1.append(self.q2.pop(0))

    def top(self):
        """
        :rtype: int
        """
        return self.q1[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not bool(self.q1)

so=Stack()
so.push(1)
so.push(2)
so.pop()
print(so.top())
