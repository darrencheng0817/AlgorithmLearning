'''
Created on 1.12.2016

@author: Darren
''''''

Given a linked list, swap every two adjacent nodes and return its head.



For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.



Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
" 
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res=ListNode(0)
        res.next=head
        cur=res
        while cur.next and cur.next.next:
            pointer1=cur.next
            pointer2=cur.next.next
            pointer1.next=pointer2.next
            pointer2.next=pointer1
            cur.next=pointer2
            cur=cur.next.next
        return res.next  
head=ListNode(1)
head.next=ListNode(2)   
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)         
so=Solution()
so.swapPairs(head)