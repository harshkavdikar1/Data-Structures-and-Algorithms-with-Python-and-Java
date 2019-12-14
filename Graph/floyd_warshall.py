'''
Created on 14-Dec-2019

@author: Harsh
'''

from graph import Graph

class FloydWarshall(Graph):
    
    def __init__(self, vertices, edges):

        super().__init__(vertices, edges)

        for i in range(len(self.vertices)):
            for j in range(len(self.vertices)):
                if i != j and self.matrix[i][j] == 0:
                    self.matrix[i][j] = float('inf')
        
        print("Iteration: Initial")
        self.display()
        print("\n")


    def all_pair_shortest_path(self):
        for k in range(len(self.vertices)):
            for i in range(len(self.vertices)):
                for j in range(len(self.vertices)):
                    # relax the distance from i to j by allowing vertex k as intermediate vertex
                    # consider which one is better, going through vertex k or the previous value
                    self.matrix[i][j] = min(self.matrix[i][j], self.matrix[i][k] + self.matrix[k][j])
            print("Iteration: ", k)
            self.display()
            print("\n")

if __name__ == "__main__":

    graph = FloydWarshall(['s', 't', 'x', 'y', 'z'],
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
 
    graph.all_pair_shortest_path()

#     graph = FloydWarshall([1, 2, 3, 4],
#           [[1, 3, -2],
#            [2, 1, 4],
#            [2, 3, 3],
#            [3, 4, 2],
#            [4, 2, -1]])
# 
#     graph.all_pair_shortest_path()