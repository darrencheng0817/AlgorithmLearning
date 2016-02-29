'''
Created on 1.12.2016

@author: Darren
'''
'''
Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.

For example:
Given binary tree,
              5
             / \
            1   5
           / \   \
          5   5   5
return 4.
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        res=[0]
        def util(root,val):
            if not root:
                return True
            if not root.left and not root.right:
                res[0]+=1
                if root.val==val:
                    return True
                else:
                    return False
            left = util(root.left,root.val)
            right = util(root.right,root.val)
            if left and right:
                res[0]+=1
                if root.val==val:
                    return True
            return False
        util(root,root.val)
        return res[0]
    
root=TreeNode(5)
root.left=TreeNode(1)
root.right=TreeNode(1)
root.left.left=TreeNode(3)
root.left.right=TreeNode(1)
root.right.left=TreeNode(1)
so=Solution()
print(so.countUnivalSubtrees(root))