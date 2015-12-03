'''
Created on 2015年12月1日
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
@author: Darren
'''

from models.BSTNode import *
from tkinter.constants import LEFT

def findLCA(root,node1,node2):
    if not root:
        return None
    if root==node1 or root==node2:
        return root
    left=findLCA(root.left, node1, node2)
    right=findLCA(root.right, node1, node2)
    if left and right:
        return root
    elif left:
        return left
    else: 
        return right

root=BSTNode(4)
root.left=BSTNode(2)
root.right=BSTNode(6)
root.left.left=BSTNode(1)
root.left.right=BSTNode(3)
root.right.left=BSTNode(5)
root.right.right=BSTNode(7)

printTreeLevelOrder(root)
print(findLCA(root, root.left.left, root.left.right))