'''
Created on 1.12.2016

@author: Darren
''''''
Given a binary tree, determine if it is height-balanced

For this problem, a height-balanced binary tree is defined as a binary tree in which 
the depth of the two subtrees of every node never differ by more than 1 
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isBalancedUtil(root)!=-1
    def isBalancedUtil(self, root):
        if not root:
            return 0
        left=self.isBalancedUtil(root.left)
        right=self.isBalancedUtil(root.right)
        if left==-1 or right==-1:
            return -1
        else:
            if abs(left-right)>1:
                return -1
            else:
                return max(left,right)+1
root=TreeNode(1)
root.right=TreeNode(2)
root.right.right=TreeNode(3)
so=Solution()
print(so.isBalanced(root))