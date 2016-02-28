'''
Created on 1.12.2016

@author: Darren
''''''

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.


For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
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
        res=ListNode(head.val-1)
        res.next=head
        valid_start=res
        pointer=head
        while pointer:
            if pointer.next and pointer.val==pointer.next.val:
                while pointer.next and pointer.val==pointer.next.val:
                    pointer=pointer.next
                valid_start.next=pointer.next
            else:
                valid_start=valid_start.next
            pointer=pointer.next
        return res.next