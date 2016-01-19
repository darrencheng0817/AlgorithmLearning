'''
Created on 1.12.2016

@author: Darren
''''''
Reverse a singly linked list
Hint:
A linked list can be reversed either iteratively or recursively. Could you implement both?
" 
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        pre,cur=None,head
        while cur:
            temp=cur.next
            cur.next=pre
            pre=cur
            cur=temp
        return pre