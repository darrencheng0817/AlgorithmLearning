'''
Created on 1.12.2016

@author: Darren
''''''
Given n, generate all structurally unique BST s (binary search trees) that store values 1...n.
For example,
Given n = 3, your program should return all 5 unique BST s shown below.


   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3



confused what "{1,#,2,3}" means? > read more on how binary tree is serialized on OJ.

OJ s Binary Tree Serialization:

The serialization of a binary tree follows a level order traversal, where  #  signifies a path terminator where no node exists below.


Here s an example:

   1
  / \
 2   3
    /
   4
    \
     5

The above binary tree is serialized as "{1,2,3,#,#,4,#,#,5}". 

" 
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n<=0:
            return []
        return self.generateTreesUtil(1,n)
    def generateTreesUtil(self, left,right): 
        if left==right:
            return [TreeNode(left)]
        if left>right:
            return [None]
        res=[]
        for value in range(left,right+1):
            for leftNode in self.generateTreesUtil(left,value-1):
                for rightNode in self.generateTreesUtil(value+1,right):
                    root=TreeNode(value)
                    root.left=leftNode
                    root.right=rightNode
                    res.append(root)
        return res