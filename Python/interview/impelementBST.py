'''
Created on 2015年12月1日

@author: Darren
'''
from Python.models.BTNode import BTNode

class BST(object):
    def __init__(self):
        self.root=None

    def insert(self,val):
        self.root=self.insertUtil(self.root, val)
        
    def insertUtil(self,root,val):
        if not root:
            root=BTNode(val)
            return root
        if val<root.value:
            root.left=self.insertUtil(root.left, val)
        else:
            root.right=self.insertUtil(root.right, val)    
        return root
    def delete(self,val):
        self.deleteUtil(self.root,val)
        
    def deleteUtil(self,root,val):
        if not root:
            return None
        if val<root.value:
            root.left=self.deleteUtil(root.left, val)
        elif val>root.value:
            root.right=self.deleteUtil(root.right, val)
        else:
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            else:
                tempNode=self.findMinNode(root.right)
                root.value=tempNode.value
                root.right=self.deleteUtil(root.right, tempNode.value)
        return root
    def findMinNode(self,root):
        if not root:
            return None
        while root.left:
            root=root.left
        return root
    def search(self,val):
        return self.searchUtil(self.root, val)
    def searchUtil(self,root,val):
        if not root:
            return False
        if val<root.value:
            return self.searchUtil(root.left, val)
        elif val>root.value:
            return self.searchUtil(root.right, val)
        else:
            return True
bst=BST()
bst.insert(2)
bst.insert(3)
print(bst.root.right)
print(bst.search(3))
print(bst.search(4))
bst.delete(3)
print(bst.root.right)
