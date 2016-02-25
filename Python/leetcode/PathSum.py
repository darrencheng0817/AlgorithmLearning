'''
Created on 1.12.2016

@author: Darren
''''''

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.


For example:
Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1



return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22." 
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right:
            return root.val==target
        return  self.hasPathSum(root.left,target-root.val) or self.hasPathSum(root.right,target-root.val)
