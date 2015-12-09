'''
Created on 2015年12月3日

@author: Darren
'''

class GraphNode(object):
    '''
    classdocs
    '''
    


    def __init__(self,value=None):
        '''
        Constructor
        '''
        self.value=value
        self.neighbor=set()
    
class Graph(object):
    
    def __init__(self):
        self.Nodes=set()
        
    def addEdge(self,NodeA,NodeB):
        NodeA.neighbor.add(NodeB)
        NodeB.neighbor.add(NodeA)
        self.Nodes.add(NodeA)
        self.Nodes.add(NodeB)
    