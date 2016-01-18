'''
Created on 2016年1月16日

@author: Darren
'''
'''
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input. 
The first node is considered odd, the second node even and so on ...


'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        oddHead,evenHead=ListNode(0),ListNode(0)
        oddPointer,evenPointer=oddHead,evenHead
        flag=1
        while head:
            if flag==1:
                oddPointer.next=head
                oddPointer=oddPointer.next
            elif flag==-1:
                evenPointer.next=head
                evenPointer=evenPointer.next
            flag*=-1
            head=head.next
        evenPointer.next=None
        oddPointer.next=evenHead.next
        return oddHead.next

def printList(head):
    res=[]
    while head:
        res.append(str(head.val))
        head=head.next
    print("->".join(res))
    
head=ListNode(0)
pointer=head
for i in range(1,6):
    next=ListNode(i)
    pointer.next=next
    pointer=pointer.next
printList(head.next)
so=Solution()
printList(so.oddEvenList(head.next))