'''
Created on 1.12.2016

@author: Darren
''''''
Given a linked list, remove the nth node from the end of list and return its head.
For example,
   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
" 
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        res=ListNode(0)
        res.next=head
        pointer1,pointer2=res,res
        for _ in range(n):
            pointer2=pointer2.next
        while pointer2.next:
            pointer2=pointer2.next
            pointer1=pointer1.next
        pointer1.next=pointer1.next.next
        return res.next