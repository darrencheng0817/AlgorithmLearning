'''
Created on 1.12.2016

@author: Darren
''''''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists." 
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res=ListNode(0)
        pointer=res
        while l1 and l2:
            if l1.val>l2.val:
                pointer.next=l2
                l2=l2.next
            else:
                pointer.next=l1
                l1=l1.next
            pointer=pointer.next
        if l1:
            pointer.next=l1
        if l2:
            pointer.next=l2
        return res.next