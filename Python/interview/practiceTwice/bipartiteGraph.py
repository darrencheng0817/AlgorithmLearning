'''
Created on 2015年12月1日
判断一个图是不是
   bipartite: https://en.wikipedia.org/wiki/Bipartite_graph

   static class Node {
                public Node() {
                        neighbors = new HashSet<Node>();
                }

                Set<Node> neighbors;
        }

        static class Graph {
                Set<Node> nodes;

                public Graph() {
                        nodes = new HashSet<Node>();
                }

                public void addEdge(Node a, Node b) {
                        a.neighbors.add(b);
                        b.neighbors.add(a);
                        nodes.add(a);
                        nodes.add(b);
                }
                public boolean isBipartite() {
                     // implement here
                     return false;
                }
        }

        public static void main(String[] args) {
                Node a = new Node();
                Node b = new Node();
                Node c = new Node();

                Graph g = new Graph();

                g.addEdge(a, b);
                g.addEdge(b, c);
                g.addEdge(c, a);

                System.out.println("is bipartite: " + g.isBipartite());
        }

@author: Darren
'''
from Python.models.Graph import *

def isBipartiteGraph(g):
    sA=set()
    sB=set()
    for node in g.Nodes:
        if node not in sB:
            sA.add(node)
            if sA&node.neighbor:
                return False
            else:
                sB|=node.neighbor
        else:
            sB.add(node)
            if sB&node.neighbor:
                return False
            else:
                sA|=node.neighbor
    return True
nodeA=GraphNode()
nodeB=GraphNode()
nodeC=GraphNode()
g=Graph()
g.addEdge(nodeA, nodeB)
g.addEdge(nodeA, nodeC)
# g.addEdge(nodeB, nodeC)
print(isBipartiteGraph(g))
