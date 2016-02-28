'''
Created on 1.12.2016

@author: Darren
''''''

Given a sorted linked list, delete all duplicates such that each element appear only once.


For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
" 
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        pre,cur=head,head.next
        while cur:
            if pre.val==cur.val:
                pre.next=cur.next
            else:
                pre=cur
            cur=cur.next
        return head
        