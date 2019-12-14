'''
Created on 14-Dec-2019

@author: Harsh
'''

from graph import Graph
from collections import deque, defaultdict

class TopologicalSort(Graph):
    
    def __init__(self, vertices, edges):

        super().__init__(vertices, edges)

    def sort(self):

        indegree = defaultdict(int)
        outdegree = defaultdict(list)

        for i in self.edges:
            indegree[i[1]] += 1
            outdegree[i[0]].append(i[1])

        queue = deque()
        count = 0

        for i in self.vertices:
            if indegree[i] == 0:
                queue.append(i)
                count+=1

        res = []
        
        while queue:

            course = queue.popleft()
            res.append(course)

            for i in outdegree[course]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
                    count+=1

        if count!=len(self.vertices):
            print("Topological Sort not possible")
        else:
            print('-->'.join(res))


if __name__ == "__main__":
    graph = TopologicalSort(['q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
                  [('q', 's', 1),
                   ('s', 'v', 1),
                   ('v', 'w', 1),
                   ('q', 'w', 1),
                   ('q', 't', 1),
                   ('t', 'x', 1),
                   ('x', 'z', 1),
                   ('t', 'y', 1),
                   ('r', 'y', 1),
                   ('r', 'u', 1),
                   ('u', 'y', 1)])

    graph.sort()