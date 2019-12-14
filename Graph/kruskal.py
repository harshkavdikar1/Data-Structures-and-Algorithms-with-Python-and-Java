'''
Created on 14-Dec-2019

@author: Harsh
'''

from graph import Graph
from union_find import UnionFind

class Kruskal(Graph):
    
    def __init__(self, vertices, edges):

        super().__init__(vertices, edges)
        self.uf = UnionFind(len(vertices))
        self.mst = []

    def kruskal_on_graph(self):
        edges = sorted(self.edges, key=lambda x: (x[2]))
        total_weight = 0

        for edge in edges:
            v1, v2, weight = edge
            if self.uf.find(self.vertices.index(v1)) != self.uf.find(self.vertices.index(v2)):
                self.uf.union(self.vertices.index(v1), self.vertices.index(v2)) 
                self.mst.append(edge)
                total_weight += weight

        print("Edges that form Minimum Spanning Tree with weight = {} are: ".format(total_weight))
        for edge in self.mst:
            print(edge)


if __name__ == "__main__":

    graph = Kruskal(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
                  [('A', 'H', 6),
                   ('H', 'A', 6),
                   ('A', 'B', 4),
                   ('B', 'A', 4),
                   ('B', 'H', 5),
                   ('H', 'B', 5),
                   ('B', 'C', 9),
                   ('C', 'B', 9),
                   ('G', 'H', 14),
                   ('H', 'G', 14),
                   ('F', 'H', 10),
                   ('H', 'F', 10),
                   ('B', 'E', 2),
                   ('E', 'B', 2),
                   ('G', 'F', 3),
                   ('F', 'G', 3),
                   ('E', 'F', 8),
                   ('F', 'E', 8),
                   ('D', 'E', 15),
                   ('E', 'D', 15)])

    graph.kruskal_on_graph()
