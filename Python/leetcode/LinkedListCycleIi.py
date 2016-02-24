'''
Created on 1.12.2016

@author: Darren
'''
'''
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
Note: Do not modify the linked list.
Follow up:
Can you solve it without using extra space
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast,slow=head,head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                fast=head
                while fast!=slow:
                    fast=fast.next
                    slow=slow.next
                return slow
        return None