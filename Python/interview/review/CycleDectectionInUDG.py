'''
Created on 2016年3月12日

@author: Darren
'''

def circle_dectector(edges,start_point):
    graph=build_graph(edges)
    queue=[start_point]
    visited=set()
    visited.add(queue[0])
    while queue:
        from_point=queue.pop(0)#BFS
        # from_point=queue.pop(0) #DFS
        for to_point in graph[from_point]:
            if to_point in visited:
                return True
            else:
                queue.append(to_point)
                visited.add(to_point)
            graph[to_point].remove(from_point)
    return False

def build_graph(edges):
    graph={}
    for from_point,to_point in edges:
        if from_point not in graph:
            graph[from_point]=set()
        if to_point not in graph:
            graph[to_point]=set()
        graph[from_point].add(to_point)
        graph[to_point].add(from_point)
    return graph
        
edges=[[1,2],[2,3],[3,4],[4,1]]
print(circle_dectector(edges),1)