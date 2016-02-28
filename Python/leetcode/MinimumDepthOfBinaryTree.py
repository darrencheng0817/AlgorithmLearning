'''
Created on 1.12.2016

@author: Darren
''''''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node." 
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left=self.minDepth(root.left)
        right=self.minDepth(root.right)
        if not left or not right:
            return left+right+1
        return min(left,right)+1