'''
Created on 14-Dec-2019

@author: Harsh
'''
from graph import Graph
from collections import deque


class BFS(Graph):
    
    def __init__(self, vertices, edges):
        super().__init__(vertices, edges)
    
    def bfs_on_graph(self, source):
        queue = deque(source)
        already_visited = {self.vertices.index(source)}
        visited = ["Edge Not Available from Source"] * len(self.vertices)
        time = 0
        while queue:
            node = queue.popleft()
            index = self.vertices.index(node)
            for i in range(len(self.matrix[index])):
                if self.matrix[index][i] == 1 and i not in already_visited:
                    already_visited.add(i)
                    queue.append(self.vertices[i])
            time += 1
            index = self.vertices.index(node)
            visited[index] = time

        self.print_discover_and_finish_time(visited)

    def print_discover_and_finish_time(self, discover):
        assert(len(discover) == len(self.vertices))
        
        for i, v in enumerate(self.vertices):
            print("Vertex: {0}\tDiscovered: {1}".format(
                    v, discover[i]))


if __name__ == "__main__":
    graph = BFS(['q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
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

    graph.bfs_on_graph('q')
