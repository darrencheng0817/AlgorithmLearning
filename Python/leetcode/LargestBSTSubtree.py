'''
Created on 2016年2月16日

@author: Darren
'''
'''
Given a binary tree, find the largest subtree which is a Binary Search Tree (BST), where largest means subtree with largest number of nodes in it.

Note:
A subtree must include all of its descendants.
Here's an example:
    10
    / \
   5  15
  / \   \ 
 1   8   7
The Largest BST Subtree in this case is the highlighted one. 
The return value is the subtree's size, which is 3.
'''
class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def Util(root):
            if not root:
                return 0,0,float('inf'),float('-inf')
            N1,n1,min1,max1=Util(root.left)
            N2,n2,min2,max2=Util(root.right)
            n=n1+n2+1 if max1<root.val<min2 else float('-inf')
            return max(N1,N2,n),n,min(min1,root.val),max(root.val,max2)
        return Util(root)[0]