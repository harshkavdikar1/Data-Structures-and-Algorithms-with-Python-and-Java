'''
Created on 14-Dec-2019

@author: Harsh
'''


class Graph():
    """All the operations are for Dense Graph"""

    def __init__(self, vertices, edges):
        super(Graph, self).__init__()
        n = len(vertices)
        self.matrix = [[0 for x in range(n)] for y in range(n)]
        self.vertices = vertices
        self.edges = edges
        for edge in edges:
            x = vertices.index(edge[0])
            y = vertices.index(edge[1])
            self.matrix[x][y] = edge[2]


    def display(self):
        print(self.vertices)
        for i, v in enumerate(self.vertices):
            print(v, self.matrix[i])


    def in_degree(self):
        print("In degree of the graph:")
        # ToDo
        indegree = [0] * len(self.vertices)
        for vertex in self.matrix:
            for j in range(len(vertex)):
                if vertex[j] != 0:
                    indegree[j] += 1
        self.print_degree(indegree)


    def out_degree(self):
        print("Out degree of the graph:")
        outdegree = [0] * len(self.vertices)
        for vertex in range(len(self.matrix)):
            for edge in self.matrix[vertex]:
                if edge != 0:
                    outdegree[vertex] += 1
        self.print_degree(outdegree)


    def print_degree(self, degree):
        assert((len(degree) == len(self.vertices)))
        for i, v in enumerate(self.vertices):
            print("Vertex: {0}\tDegree: {1}".format(v, degree[i]))

if __name__ == "__main__":
    g = Graph(['q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
              [('q', 's', 1),
               ('s', 'v', 1),
               ('v', 'w', 1),
               ('w', 's', 1),
               ('q', 'w', 1),
               ('q', 't', 1),
               ('t', 'x', 1),
               ('x', 'z', 1),
               ('z', 'x', 1),
               ('t', 'y', 1),
               ('y', 'q', 1),
               ('r', 'y', 1),
               ('r', 'u', 1),
               ('u', 'y', 1)])

    g.display()

    g.in_degree()

    g.out_degree()