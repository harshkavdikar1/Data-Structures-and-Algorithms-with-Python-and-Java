'''
Created on 14-Dec-2019

@author: Harsh
'''

from graph import Graph

class DFS(Graph):
    
    def __init__(self, vertices, edges):

        super().__init__(vertices, edges)


    def dfs_on_graph(self):

        visited = [0] * len(self.vertices)
        finished = [0] * len(self.vertices)
        already_visited = set()
        timer = 0

        for vertex in self.vertices:
            if vertex not in already_visited:
                timer = self.dfs(vertex, visited, finished, already_visited, timer)

        self.print_discover_and_finish_time(visited, finished)


    def dfs(self, node, visited, finished, already_visited, timer):

        index = self.vertices.index(node)
    
        if node in already_visited:
            return timer
    
        already_visited.add(node)
        timer += 1
        visited[index] = timer
    
        for i in range(len(self.matrix[index])):
            if self.matrix[index][i] == 1:
                timer = self.dfs(self.vertices[i], visited, finished, already_visited, timer)
    
        timer += 1
        finished[index] = timer
    
        return timer

    def print_discover_and_finish_time(self, discover, finish):
        assert((len(discover) == len(self.vertices)) and
               (len(finish) == len(self.vertices)))
        
        for i, v in enumerate(self.vertices):
            print("Vertex: {0}\tDiscovered: {1}\tFinished: {2}".format(
                    v, discover[i], finish[i]))


if __name__ == "__main__":
    graph = DFS(['q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
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
    
    graph.dfs_on_graph()