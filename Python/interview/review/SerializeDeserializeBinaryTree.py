'''
Created on 2016年2月29日

@author: Darren
'''
class TreeNode(object):
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
def serialize(root):
    res=[]
    def util(root):
        if not root:
            res.append("#")
            return
        res.append(root.val)
        util(root.left)
        util(root.right)
    util(root)
    return " ".join(list(map(str,res)))

def deserialize(string):
    l=iter(string.split(" "))
    def util():
        val=next(l)
        if val=="#":
            return None
        root=TreeNode(val)
        root.left=util()
        root.right=util()
        return root
    return util()

root=TreeNode(1)
root.left=TreeNode(3)
root.right=TreeNode(4)
string=serialize(root)
print(string)
new_root=deserialize(string)
print(new_root.val)