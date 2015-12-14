'''
Created on 2015年12月1日
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
@author: Darren
'''
import models
from models.BTNode import *

def findLCA(root,node1,node2):
    pass

def findLCA2(root,value1,value2):
    '''
    if node1 is the ancestor of node 2, return node1's lowest ancestor
    '''
    pass  

root=BTNode(4)
root.left=BTNode(2)
root.right=BTNode(6)
root.left.left=BTNode(1)
root.left.right=BTNode(3)
root.right.left=BTNode(5)
root.right.right=BTNode(7)

printTreeLevelOrder(root)
print(findLCA(root, root.left.left, root.left.right))
print(findLCA2(root, 1, 2))