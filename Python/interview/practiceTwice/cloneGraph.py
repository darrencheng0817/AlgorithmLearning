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
        queue=[node]
        newNode=UndirectedGraphNode(node.label)
        dic={}
        dic[node]=newNode
        while queue:
            curNode=queue.pop()
            targetNode=dic[curNode]
            for neighbor in curNode.neighbors:
                if neighbor not in dic:
                    newNode=UndirectedGraphNode(neighbor.label)
                    dic[neighbor]=newNode
                    queue.append(neighbor)
                targetNode.neighbors.append(dic[neighbor])
        return dic[node]