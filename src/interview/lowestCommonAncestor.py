'''
Created on 2015年12月1日
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
@author: Darren
'''

from src.models.BTNode import *

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

root=BTNode(4)
root.left=BTNode(2)
root.right=BTNode(6)
root.left.left=BTNode(1)
root.left.right=BTNode(3)
root.right.left=BTNode(5)
root.right.right=BTNode(7)

printTreeLevelOrder(root)
print(findLCA(root, root.left.left, root.left.right))