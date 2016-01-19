'''
Created on 1.12.2016

@author: Darren
''''''
Reverse a linked list from position m to n. Do it in-place and in one-pass.
For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4
return 1->4->3->2->5->NULL.
Note:
Given m, n satisfy the following condition:
1 <= m <= n <=length of list.
" 
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        res=ListNode(0)
        res.next=head
        pointer=res
        for counter in range(m-1):
            pointer=pointer.next
        start=pointer
        pointer=pointer.next
        for counter in range(n-m):
            next=pointer.next
            pointer.next=next.next
            next.next=start.next
            start.next=next
        return res.next
            
        