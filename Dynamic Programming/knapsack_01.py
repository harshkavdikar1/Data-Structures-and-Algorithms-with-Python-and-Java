'''
Created on 28-Nov-2019

@author: Harsh
'''


def knapsack(size, items):
    m = len(items)
    matrix = [[0 for _ in range(size + 1)] for _ in range(m + 1)]
    items = sorted(items)
    for i in range(1, m + 1):
        for j in range(1, size + 1):
            weight, value = items[i - 1]
            if weight > j:
                matrix[i][j] = matrix[i - 1][j]
            else:
                matrix[i][j] = max(matrix[i - 1][j], value + matrix[i - 1][j - weight])
    return matrix[-1][-1]


if __name__ == '__main__':
    size = 20
    items = [(2, 3), (3, 4), (4, 5), (5, 8), (9, 10)]
    assert(knapsack(size, items) == 26)
