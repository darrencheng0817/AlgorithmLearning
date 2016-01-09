'''
Created on 2016年1月6日

@author: Darren
'''
'''
Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its vertical order traversal as:
[
  [9],
  [3,15],
  [20],
  [7]
]
Given binary tree [3,9,20,4,5,2,7],
    _3_
   /   \
  9    20
 / \   / \
4   5 2   7
return its vertical order traversal as:
[
  [4],
  [9],
  [3,5,2],
  [20],
  [7]
]
Show Company Tags
Show Tags
Show Similar Problems
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
        
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res=[]
        queue=[(0,root)]
        d={}
        while queue:
            verticalIndex,cur=queue.pop(0)
            if verticalIndex not in d:
                d[verticalIndex]=[]
            d[verticalIndex].append(cur.val)
            if cur.left:
                queue.append((verticalIndex-1,cur.left))
            if cur.right:
                queue.append((verticalIndex+1,cur.right))
        for key in sorted(d.keys()):
            res.append(d[key])
        return res
        