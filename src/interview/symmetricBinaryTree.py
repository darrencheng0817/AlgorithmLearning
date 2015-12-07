'''
Created on 2015年12月1日
https://leetcode.com/problems/symmetric-tree/
@author: Darren
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def isSymmetric(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if not root:
        return True
    leftPart=[root.left]
    rightPart=[root.right]
    while leftPart and rightPart:
        leftNode=leftPart.pop()
        rightNode=rightPart.pop()
        if leftNode and rightNode:
            if leftNode.val!=rightNode.val:
                return False
            leftPart.append(leftNode.left)
            leftPart.append(leftNode.right)
            rightPart.append(rightNode.right)
            rightPart.append(rightNode.left)
        elif leftNode or rightNode:
            return False
    return True

def isSymmetric2(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if not root:
        return True
    return isSymmetricUtil(root.left,root.right)

def isSymmetricUtil(left,right):
    if left and right:
        if left.val!=right.val:
            return False
        else:
            return isSymmetricUtil(left.left,right.right) and isSymmetricUtil(left.right,right.left)
    elif left or right:
        return False
    else:
        return True