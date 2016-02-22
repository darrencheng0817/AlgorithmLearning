'''
Created on 1.12.2016

@author: Darren
'''
'''
Given a binary tree, return all root-to-leaf paths.
For example, given the following binary tree:
   1
 /   \
2     3
 \
  5

All root-to-leaf paths are:
["1->2->5", "1->3"]
Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases." 
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        res=[]
        def util(root,path,res):
            if not root.left and not root.right:
                res.append("->".join(path+[str(root.val)]))
                return
            if root.left:
                util(root.left,path+[str(root.val)],res)
            if root.right:
                util(root.right,path+[str(root.val)],res)
        util(root,[],res)
        return res