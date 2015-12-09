'''
Created on 2015年12月6日
Given a binary tree, return the vertical order traversal of its nodes' values. (ie, from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

Examples:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its vertical order traversal as:
[
  [9],
  [3,15],
  [20],
  [7]
]
Given binary tree [3,9,20,4,5,2,7],
    _3_
   /   \
  9    20
 / \   / \
4   5 2   7
return its vertical order traversal as:
[
  [4],
  [9],
  [3,5,2],
  [20],
  [7]
]
@author: Darren
'''
def verticalOrder( root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    map={}
    queue=[(root,0)]
    while queue:
        node,level=queue.pop(0)
        if node:
            if level not in map:
                map[level]=[]
            map[level].append(node.val)
            queue.append((node.left,level-1))
            queue.append((node.right,level+1))
    return [map[i] for i in sorted(map.keys())]