'''
Created on 2015年12月1日
https://leetcode.com/problems/clone-graph/
@author: Darren
'''

# Definition for a undirected graph node
class UndirectedGraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if not node:
            return None
        m={}
        newRoot=UndirectedGraphNode(node.label)
        m[node]=newRoot
        queue=[node]
        while queue:
            tempNode=queue.pop(0)
            for n in tempNode.neighbors:
                if n not in m:
                    newNode=UndirectedGraphNode(n.label)
                    m[n]=newNode
                    queue.append(n)
                m[tempNode].neighbors.append(m[n])
        return newRoot