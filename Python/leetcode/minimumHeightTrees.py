'''
Created on 2015年12月12日
https://leetcode.com/problems/minimum-height-trees/
@author: Darren
'''
'''
For a undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example 1:

Given n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3
return [1]

Example 2:

Given n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5
return [3, 4]
'''
def findMinHeightTrees(n, edges):
    """
    :type n: int
    :type edges: List[List[int]]
    :rtype: List[int]
    """
    if not edges or n==1:
        return [0]
    adj=[set() for i in range(n)]
    for i,j in edges:
        adj[i].add(j)
        adj[j].add(i)
    leaves=[nodeIndex for nodeIndex in range(n) if len(adj[nodeIndex])==1]
    while n>2:
        n-=len(leaves)
        newLeaves=[]
        for leaf in leaves:
            adjLeaf=adj[leaf].pop()
            adj[adjLeaf].remove(leaf)
            if len(adj[adjLeaf])==1:
                newLeaves.append(adjLeaf)
        leaves=newLeaves
    return leaves
n = 6
edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]       
print(findMinHeightTrees(n, edges)) 
    