'''
Created on 2015年12月1日
给一个DAG, 求出进行inorder traversal后的第k个node。此DAG上每个node out degrees最大为2.但是in degree可以大于2。
这个题目我当时没做出来。因为一个点可以被visit好多次。面试官提醒说运行时间是exponential，
@author: Darren
'''

def findKth(node,k):
    cache={}
    return findKthUtil(cache, node, k)

def findKthUtil(cache,node,k):
    leftCount=countNode(cache,node.left)
    if leftCount==k+1:
        return node
    elif leftCount<=k:
        return findKthUtil(node.left, k)
    else:
        return findKthUtil(node.right, k-leftCount-1)
    
def countNode(cache,node):
    if not node:
        return 0
    if node in cache:
        return cache[node]
    count=1+countNode(cache,node.left)+countNode(cache,node.right)
    cache[node]=count
    return count