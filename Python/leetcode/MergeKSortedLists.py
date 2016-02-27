'''
Created on 1.12.2016

@author: Darren
''''''

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
" 
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        res=ListNode(0)
        pointer=res
        lists=[v for v in lists if v]
        while lists:
            lists=sorted(lists,key=lambda x:x.val,reverse=True)
            pointer.next=lists.pop()
            pointer=pointer.next
            if pointer.next:
                lists.append(pointer.next)
        return res.next
    
    def mergeKLists2(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        from heapq import heappush, heappop, heapreplace, heapify
        dummy = node = ListNode(0)
        h = [(n.val, n) for n in lists if n]
        heapify(h)
        while h:
            v, n = h[0]
            if n.next is None:
                heappop(h) #only change heap size when necessary
            else:
                heapreplace(h, (n.next.val, n.next))
            node.next = n
            node = node.next
    
        return dummy.next
l1=ListNode(1)
l1.next=ListNode(2)
l1.next.next=ListNode(4)
l2=ListNode(3)
l2.next=ListNode(4)
l2.next.next=ListNode(5)   
so=Solution()
so.mergeKLists([l1,l2])  