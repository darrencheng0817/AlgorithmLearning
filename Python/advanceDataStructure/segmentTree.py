'''
Created on 2015年12月12日
Implementation of segmentTree, this demo is used to query the sum of a range 
refer http://blog.csdn.net/metalseed/article/details/8039326
@author: Darren
'''
class SegmentTreeNode(object):
    def __init__(self,leftIndex=0,rightIndex=0,value=0):
        self.leftIndex=leftIndex
        self.rightIndex=rightIndex
        self.value=value
        self.left=None
        self.right=None
        
class SegmentTree(object):
    def __init__(self):
        self.root=None
    
    def build(self,array):
        self.root=self.buildUtil(self.root,array,0,len(array)-1)
        
    def buildUtil(self,root,array,leftIndex,rightIndex):
        if not root:
            root=SegmentTreeNode(leftIndex,rightIndex)
        if leftIndex==rightIndex:
            root.value=array[leftIndex]
        else:
            midIndex=(leftIndex+rightIndex)//2
            root.left=self.buildUtil(root.left,array,leftIndex,midIndex)
            root.right=self.buildUtil(root.right, array, midIndex+1, rightIndex)
            if root.left:
                root.value+=root.left.value
            if root.right:
                root.value+=root.right.value
        return root
    def update(self,index,value):
        self.updateUtil(self.root,index,value)
        
    def updateUtil(self,root,index,value):
        diff=0
        if root.leftIndex==root.rightIndex:
            diff=value-root.value
            root.value=value
            return diff
        midIndex=(root.leftIndex+root.rightIndex)//2
        if index<=midIndex:
            diff=self.updateUtil(root.left,index,value)
        else:
            diff=self.updateUtil(root.right,index,value)
        root.value+=diff
        return diff
    
    def query(self,indexI,indexJ):    
        return self.queryUtil(self.root, indexI, indexJ)
    
    def queryUtil(self,root,indexI,indexJ):
        if root.leftIndex==indexI and root.rightIndex==indexJ:
            return root.value      
        midIndex=(root.leftIndex+root.rightIndex)//2
        if indexJ<=midIndex:
            return self.queryUtil(root.left, indexI, indexJ)
        elif indexI>midIndex:
            return self.queryUtil(root.right, indexI, indexJ)
        else:
            return self.queryUtil(root.left, indexI, midIndex)+self.queryUtil(root.right, midIndex+1, indexJ)
        
segmentTree=SegmentTree()
array=[1,2,3,4,5,6,7,8]
segmentTree.build(array)
print(segmentTree.query(1,3))
segmentTree.update(3, 10)
