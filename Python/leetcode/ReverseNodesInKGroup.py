'''
Created on 1.12.2016

@author: Darren
'''
'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
You may not alter the values in the nodes, only nodes itself may be changed
Only constant memory is allowed
For example,
Given this linked list: 1->2->3->4->5For k = 2, you should return: 2->1->4->3->5
For k = 3, you should return: 3->2->1->4->5
" 
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __str__(self, *args, **kwargs):
        return str(self.val)
    
    def __repr__(self, *args, **kwargs):
        return str(self.val)
    
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = jump = ListNode(0)
        dummy.next = l = r = head
    
        while True:
            count = 0
            while r and count < k:   # use r to locate the range
                r = r.next
                count += 1
            if count == k:  # if size k satisfied, reverse the inner linked list
                pre, cur = r, l
                for _ in range(k):
                    cur.next, cur, pre = pre, cur.next, cur  # standard reversing
                jump.next, jump, l = pre, l, r  # connect two k-groups
            else:
                return dummy.next

l=ListNode(1)
l.next=ListNode(2)
l.next.next=ListNode(3)
l.next.next.next=ListNode(4)
l.next.next.next.next=ListNode(5)      
so=Solution()
so.reverseKGroup(l,2)  