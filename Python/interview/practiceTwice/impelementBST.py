'''
Created on 2015年12月1日

@author: Darren
'''

class BTNode(object):
    def __init__(self,value=None):
        self.value=value
        self.left=None
        self.right=None
    def __repr__(self):
        return str(self.value) 
    
class BST(object):
    def __init__(self):
        self.root=None

    def insert(self,val):
        self.root=self.__insertUitl(self.root, val)
        
    def __insertUitl(self,root,val):
        if not root:
            return BTNode(val)
        if val>root.value:
            root.right=self.__insertUitl(root.right, val)
        else:
            root.left=self.__insertUitl(root.left, val)
        return root
    
    def delete(self,val):
        self.root=self.__deleteUtil(self.root, val)
    
    def __getSuccessor(self,node):
        if not node:
            return None
        while node.left:
            node=node.left
        return node
    
    def __deleteUtil(self,root,val):
        if not root:
            return None
        if val>root.value:
            root.right=self.__deleteUtil(root.right, val)
        elif val<root.value:
            root.left=self.__deleteUtil(root.left, val)
        else:
            if not root.left and not root.right:
                return None
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                nextNode=self.__getSuccessor(root.right)
                root.value=nextNode.value
                root.right=self.__deleteUtil(root.right, nextNode.value)
        return root
    
    def search(self,val):
        return self.__searchUtil(self.root, val)
    def __searchUtil(self,root,val):
        if not root:
            return False
        if root.value==val:
            return True
        elif root.value<val:
            return self.__searchUtil(root.right, val)
        else:
            return self.__searchUtil(root.left, val)
bst=BST()
bst.insert(2)
bst.insert(3)
print(bst.root.right)
print(bst.search(3))
print(bst.search(4))
bst.delete(3)
print(bst.root.right)
