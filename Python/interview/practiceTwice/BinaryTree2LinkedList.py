'''
Created on 2015年12月1日
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
@author: Darren
'''
class BTNode(object):
    def __init__(self,value):
        self.left=None
        self.right=None
        self.value=value
    def __repr__(self):
        return str(self.value)

class Solution(object):
    def __init__(self):
        self.pre=None
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        rightNode=root.right
        if not self.pre:
            self.pre=root
        else:
            self.pre.left=None
            self.pre.right=root
            self.pre=root
        self.flatten(root.left)
        self.flatten(rightNode)


