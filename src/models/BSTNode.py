'''
Created on 2015年12月3日

@author: Darren
'''
class BSTNode(object):
    def __init__(self,value):
        self.left=None
        self.right=None
        self.value=value
    def __repr__(self):
        return str(self.value)

def printTreeLevelOrder(root):
    if not root:
        print("Empty Tree!")
        return
    queue=[root]
    while queue:
        print(" ".join([str(node.value) for node in queue]))
        newQueue=[]
        for node in queue:
            if node.left:
                newQueue.append(node.left)
            if node.right:
                newQueue.append(node.right)
        queue=newQueue
        

def buildTreeUtil(preOrder,index):
    if not preOrder or len(preOrder)<=index[0] or preOrder[index[0]]=="#":
        index[0]+=1
        return None
    root=BSTNode(preOrder[index[0]])
    index[0]+=1
    root.left=buildTreeUtil(preOrder, index)
    root.right=buildTreeUtil(preOrder, index)
    return root

def buildTree(preOrder):
    return buildTreeUtil(preOrder, [0])
    