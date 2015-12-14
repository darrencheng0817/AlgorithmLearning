'''
Created on 2015年12月1日

@author: Darren
'''
from src.models.BTNode import BTNode

class BST(object):
    def __init__(self):
        self.root=None

    def insert(self,val):
        pass
    def delete(self,val):
        pass
bst=BST()
bst.insert(2)
bst.insert(3)
print(bst.root.right)
print(bst.search(3))
print(bst.search(4))
bst.delete(3)
print(bst.root.right)
