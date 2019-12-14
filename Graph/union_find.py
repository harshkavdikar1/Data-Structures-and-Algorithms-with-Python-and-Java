'''
Created on 14-Dec-2019

@author: Harsh
'''

class UnionFind():

    def __init__(self, N):
        self.A = list(range(N))

    def union(self, x, y):
        self.A[self.find(x)] = self.find(y)

    def find(self, x):
        if self.A[x] != x:
            self.A[x] = self.find(self.A[x])
        return self.A[x]