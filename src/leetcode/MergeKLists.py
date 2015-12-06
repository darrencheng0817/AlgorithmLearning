
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
        from heapq import heappush, heappop, heapreplace, heapify
        h=[]
        res=ListNode(0)
        p=res
        h = [(n.val, n) for n in lists if n]
        heapify(h)
        while h:
            value,minNode=h[0]
            p.next=minNode
            if not minNode.next:
                heappop(h)
            else:
                heapreplace(h,(minNode.next.val,minNode.next))
            p=p.next
        return res.next
    
    def mergeKLists2(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        from heapq import heappush, heappop, heapreplace, heapify
        h=[]
        res=ListNode(0)
        p=res
        for n in lists:
            if n:
                h.append((n.val,n))
        heapify(h)
        while h:
            value,minNode=heappop(h)
            p.next=minNode
            if minNode.next:
                heappush(h, (minNode.next.val,minNode.next))
            p=p.next
        return res.next

so=Solution()
l1=ListNode(3)
l1.next=ListNode(5)
l1.next.next=ListNode(6)
l2=ListNode(7)
l2.next=ListNode(9)
input=[l1,l2]
res=so.mergeKLists2(input)
while res:
    print(res.val)
    res=res.next
