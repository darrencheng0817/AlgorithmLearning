'''
Created on 2015年12月15日

@author: Darren
'''

def inOrder(root):
    res=[]
    stack=[]
    while root or stack:
        if root:
            stack.append(root.val)
            root=root.left
        else:
            root=stack.pop()
            res.append(root.val)
            root=root.right
    return res

def preOrder(root):
    res=[]
    stack=[]
    while root or stack:
        if root:
            res.append(root.val)
            stack.append(root)
            root=root.left
        else:
            root=stack.pop()
            root=root.right
    return res

def postOrder(root):
    res=[]
    stack=[]
    preNode=None
    while root or stack:
        if root:
            stack.append(root)
            root=root.Left
        else:
            peekNode=stack[-1]
            if peekNode.right and preNode!=peekNode.right:
                root=peekNode.right
            else:
                stack.pop()
                res.append(peekNode.val)
                preNode=peekNode
    return res            
  
def preOrder2(root):
    if not root:
        return 
    print(root.val)
    preOrder(root.left)
    preOrder(root.right)

def inOrder2(root):
    if not root:
        return
    inOrder(root.left)
    print(root.val)
    inOrder(root.right)
    
def postOrder2(root):
    if not root:
        return 
    postOrder(root.left)
    postOrder(root.right)
    print(root.val)
    