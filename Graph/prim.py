'''
Created on 14-Dec-2019

@author: Harsh
'''

from graph import Graph
import heapq

class Prim(Graph):
    
    def __init__(self, vertices, edges):

        super().__init__(vertices, edges)



    def prim(self, root):

        distance = [float('inf')] * len(self.vertices)

        distance[self.vertices.index(root)] = 0

        pi = [None] * len(self.vertices)

        queue = [[0, root]]

        already_visited = set()

        iteration = -1

        self.print_d_and_pi('Initial', distance, pi)

        while queue:
            current_node = heapq.heappop(queue)[1]

            if current_node in already_visited:
                continue

            already_visited.add(current_node)
            node = self.vertices.index(current_node)

            for neighbour, edge_weight in enumerate(self.matrix[node]):

                if edge_weight > 0:
                    heapq.heappush(queue, [edge_weight, self.vertices[neighbour]])

                    if distance[neighbour] > edge_weight:
                        distance[neighbour] = edge_weight
                        pi[neighbour] = current_node

            iteration += 1
            self.print_d_and_pi(iteration, distance, pi)



    def print_d_and_pi(self, iteration, d, pi):
        assert((len(d) == len(self.vertices)) and
               (len(pi) == len(self.vertices)))

        print("Iteration: {0}".format(iteration))
        for i, v in enumerate(self.vertices):
            print("Vertex: {0}\td: {1}\tpi: {2}".format(v, 'inf' if d[i] == float("inf") else d[i], pi[i]))


if __name__ == "__main__":

    graph = Prim(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'],
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

    graph.prim('G')
