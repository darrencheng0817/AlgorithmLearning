'''
Created on 1.12.2016

@author: Darren
''''''
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
" 
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return None
        root_value=postorder.pop()
        root_index=inorder.index(root_value)
        root=TreeNode(root_value)
        root.right=self.buildTree(inorder[root_index+1:],postorder)
        root.left=self.buildTree(inorder[:root_index],postorder)
        return root