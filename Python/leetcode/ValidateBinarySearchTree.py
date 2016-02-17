'''
Created on 1.12.2016

@author: Darren
''''''

Given a binary tree, determine if it is a valid binary search tree (BST).



Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node s key.
The right subtree of a node contains only nodes with keys greater than the node s key.
Both the left and right subtrees must also be binary search trees.



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
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def util(root,min_value,max_value):
            if not root:
                return True
            if not min_value<root.val<max_value:
                return False
            return util(root.left,min_value,root.val) and util(root.right,root.val,max_value)
        return util(root,float('-inf'),float('inf'))
    
    def isValidBST2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def util(root):
            if not root:
                return True,float('inf'),float('-inf')
            flag1,min1,max1=util(root.left)
            flag2,min2,max2=util(root.right)
            if flag1 and flag2 and max1<root.val<min2:
                return True,min(root.val,min1),max(root.val,max2)
            return False,min(root.val,min1),max(root.val,max2)
        return util(root)[0]
    
    def isValidBST3(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        pre=[None]
        def util(root):
            if not root:
                return True
            left=util(root.left)
            if pre[0]!=None and root.val<=pre[0].val:
                return False
            pre[0]=root
            return left and util(root.right)
            
        return util(root)
