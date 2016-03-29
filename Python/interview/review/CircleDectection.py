'''
Created on 2016年2月29日

@author: Darren
'''

def circle_dectector(edges):
    graph,in_degree=build_graph(edges)
    queue=[start_point for start_point in in_degree.keys() if in_degree[start_point]==0]
    while queue:
        from_point=queue.pop(0)
        for to_point in graph[from_point]:
            in_degree[to_point]-=1
            if in_degree[to_point]==0:
                queue.append(to_point)
        graph.pop(from_point)
    return not bool(graph)

def circle_dectector_dfs(edges):
    graph,in_degree=build_graph(edges)
    visited=set()
    rec_stack=set()
    def dfs(point):
        if point in visited:
            return True
        visited.add(point)
        rec_stack.add(point)
        for to_point in graph[point]:
            if to_point not in visited and not dfs(to_point):
                return False
            elif to_point in rec_stack:
                return False
        rec_stack.remove(point)
        return True   
    for point in graph.keys():
        if not dfs(point):
            return False      
    return True

def build_graph(edges):
    graph={}
    in_degree={}
    for from_point,to_point in edges:
        if from_point not in graph:
            graph[from_point]=[]
        if to_point not in graph:
            graph[to_point]=[]
        graph[from_point].append(to_point)
        if from_point not in in_degree:
            in_degree[from_point]=0
        if to_point not in in_degree:
            in_degree[to_point]=0
        in_degree[to_point]+=1
    return graph,in_degree
        

edges=[[1,2],[2,3],[3,4],[4,4]]
print(circle_dectector(edges))
print(circle_dectector_dfs(edges))