'''
Created on 1.12.2016

@author: Darren
''''''

Given a binary tree and a sum, find all root-to-leaf paths where each path s sum equals the given sum.


For example:
Given the below binary tree and sum = 22,

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1



return

[
   [5,4,11,2],
   [5,8,4,5]
]

" 
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res=[]
        def util(root,target,items):
            if not root:
                return
            if not root.left and not root.right:
                if target==root.val:
                    res.append(items+[root.val])
                return
            util(root.left,target-root.val,items+[root.val])
            util(root.right,target-root.val,items+[root.val])
        util(root,target,[])
        return res