'''
Created on 1.12.2016

@author: Darren
'''
'''
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), 
write a function to find the number of connected components in an undirected graph.

Example 1:
     0          3
     |          |
     1 --- 2    4
Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.

Example 2:
     0           4
     |           |
     1 --- 2 --- 3
Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.


'''
class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        unvisited=set(list(range(n)))
        graph={}
        for edge in edges:
            if edge[0] not in graph:
                graph[edge[0]]=[]
            if edge[1] not in graph:
                graph[edge[1]]=[]
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        res=0
        while unvisited:
            queue=[unvisited.pop()]
            res+=1
            while queue:
                node=queue.pop()
                if node not in graph:
                    continue
                for adjNode in graph[node]:
                    if adjNode in unvisited:
                        unvisited.remove(adjNode)
                        queue.append(adjNode)
        return res   

n=5
edges=[[0,1],[1,2],[3,4]]
so=Solution()
print(so.countComponents(n, edges))