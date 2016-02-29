'''
Created on 1.12.2016

@author: Darren
''''''

Given a binary tree, find the maximum path sum.


For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path does not need to go through the root.


For example:
Given the below binary tree,

       1
      / \
     2   3



Return 6.
" 
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res=[float("-inf")]
        def util(root):
            if not root:
                return 0
            left=util(root.left)
            right=util(root.right)
            res[0]=max(res[0],left+right+root.val,left+root.val,right+root.val,root.val)
            return max(left,right,0)+root.val
        util(root)
        return res[0]