'''
Created on 14-Dec-2019

@author: Harsh
'''

from graph import Graph

class BellmanFord(Graph):
    
    def __init__(self, vertices, edges):

        super().__init__(vertices, edges)



    def bellman_ford(self, source):

        distance = [float('inf')] * len(self.vertices)

        pi = [None] * len(self.vertices)

        distance[self.vertices.index(source)] = 0

        self.print_d_and_pi('Initial', distance, pi)

        iteration = -1

        for _ in range(len(self.vertices) - 1):

            for u, v, w in self.edges:

                u = self.vertices.index(u)
                v = self.vertices.index(v)

                if distance[v] > distance[u] + w:
                    distance[v] = distance[u] + w
                    pi[v] = self.vertices[u]

            iteration += 1
            self.print_d_and_pi(iteration, distance, pi)

        for u, v, w in self.edges:

            u = self.vertices.index(u)
            v = self.vertices.index(v)

            if distance[v] > distance[u] + w:
                print('No Solution')



    def print_d_and_pi(self, iteration, d, pi):
        assert((len(d) == len(self.vertices)) and
               (len(pi) == len(self.vertices)))

        print("Iteration: {0}".format(iteration))
        for i, v in enumerate(self.vertices):
            print("Vertex: {0}\td: {1}\tpi: {2}".format(v, 'inf' if d[i] == float("inf") else d[i], pi[i]))



if __name__ == "__main__":

    graph = BellmanFord(['s', 't', 'x', 'y', 'z'],
              [('t', 'x', 5),
               ('t', 'y', 8),
               ('t', 'z', -4),
               ('x', 't', -2),
               ('y', 'x', -3),
               ('y', 'z', 9),
               ('z', 'x', 7),
               ('z', 's', 2),
               ('s', 't', 6),
               ('s', 'y', 7)])
    graph.bellman_ford('z')

#     graph = BellmanFord(['s', 't', 'x', 'y', 'z'],
#                   [('t', 'x', 5),
#                    ('t', 'y', 8),
#                    ('t', 'z', -4),
#                    ('x', 't', -2),
#                    ('y', 'x', -3),
#                    ('y', 'z', 9),
#                    ('z', 'x', 4),
#                    ('z', 's', 2),
#                    ('s', 't', 6),
#                    ('s', 'y', 7)])
#     graph.bellman_ford('s')