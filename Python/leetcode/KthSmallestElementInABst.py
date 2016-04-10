'''
Created on 1.12.2016

@author: Darren
''''''
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 
You may assume k is always valid, 1 �� k �� BST s total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?


  Try to utilize the property of a BST.
  What if you could modify the BST node s structure?
  The optimal runtime complexity is O(height of BST).


Credits:Special thanks to @ts for adding this problem and creating all test cases." 
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack=[]
        while root or stack:
            if root:
                stack.append(root)
                root=root.left
            else:
                root=stack.pop()
                k-=1
                if k==0:
                    return root.val
                root=root.right
                
