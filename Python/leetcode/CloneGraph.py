'''
Created on 1.12.2016

@author: Darren
''''''

Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.




OJ s undirected graph serialization:


Nodes are labeled uniquely.


We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.




As an example, consider the serialized graph {0,1,2#1,2#2,2}.



The graph has a total of three nodes, and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.




Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/



" 
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