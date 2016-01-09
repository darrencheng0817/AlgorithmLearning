'''
Created on 2016年1月8日

@author: Darren
'''
'''
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return None
        elif not l1:
            return l2
        elif not l2:
            return l1
        res=ListNode(0)
        pointer=res
        carry=0
        while l1 or l2 or carry!=0:
            valueSum=carry
            if l1:
                valueSum+=l1.val
                l1=l1.next
            if l2:
                valueSum+=l2.val
                l2=l2.next
            pointer.next=ListNode(valueSum%10)
            carry=valueSum//10
            pointer=pointer.next
        return res.next
                