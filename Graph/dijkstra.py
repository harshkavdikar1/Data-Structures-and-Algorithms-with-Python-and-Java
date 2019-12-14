'''
Created on 14-Dec-2019

@author: Harsh
'''


from graph import Graph
import heapq

class Dijkstra(Graph):
    
    def __init__(self, vertices, edges):

        super().__init__(vertices, edges)

    def dijkstra(self, source):

        distance = [float('inf')] * len(self.vertices)

        pi = [None] * len(self.vertices)

        queue = [[0, source]]

        already_visited = set()

        iteration = -1

        distance[self.vertices.index(source)] = 0

        self.print_d_and_pi('Initial', distance, pi)

        while queue:
            weight, current_node = heapq.heappop(queue)

            if current_node in already_visited:
                continue

            already_visited.add(current_node)
            node = self.vertices.index(current_node)

            for neighbour, edge_weight in enumerate(self.matrix[node]):

                if edge_weight > 0:

                    heapq.heappush(queue, [weight + edge_weight, self.vertices[neighbour]])

                    if distance[neighbour] > weight + edge_weight:
                        distance[neighbour] = weight + edge_weight
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

    graph = Dijkstra(['s', 't', 'x', 'y', 'z'],
              [('s', 't', 3),
               ('s', 'y', 5),
               ('t', 'x', 6),
               ('t', 'y', 2),
               ('x', 'z', 2),
               ('y', 't', 1),
               ('y', 'x', 4),
               ('y', 'z', 6),
               ('z', 's', 3),
               ('z', 'x', 7)])

    graph.dijkstra('s')