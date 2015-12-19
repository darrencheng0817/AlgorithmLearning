'''
Created on 2015年12月1日
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
@author: Darren
'''

from Python.models.BTNode import *

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

def findLCA2(root,value1,value2):
    '''
    if node1 is the ancestor of node 2, return node1's lowest ancestor
    '''
    res=[]
    targets=set([value1,value2])
    findLCA2Util(root, targets, res, [])
    index=0
    while index<len(res[0]) and index<len(res[1]):
        if res[0][index]!=res[1][index]:
            return res[0][index-1]
        index+=1
    if index==len(res[0]):
        return res[0][-1]
    if index==len(res[1]):
        return res[1][-1]    

def findLCA2Util(root,targets,res,path):
    if not root:
        return
    if root.value in targets:
        res.append(path)
        targets.remove(root.value)
        if not targets:
            return
    findLCA2Util(root.left, targets, res, path+[root.value])
    findLCA2Util(root.right, targets, res, path+[root.value])
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