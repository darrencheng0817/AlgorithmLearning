'''
Created on 1.12.2016

@author: Darren
''''''
Given an array where elements are sorted in ascending order, convert it to a height balanced BST." 
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        m=len(nums)//2
        root=TreeNode(nums[m])
        root.left=self.sortedArrayToBST(nums[:m])
        root.right=self.sortedArrayToBST(nums[m+1:])
        return root