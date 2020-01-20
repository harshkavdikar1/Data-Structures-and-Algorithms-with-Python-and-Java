'''
Created on 28-Nov-2019

@author: Harsh
'''


def LCS(s1, s2):
    m = len(s1)
    n = len(s2)
    matrix = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])
    
    A = []
    i = m
    j = n
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            A.append(s1[i - 1])
            i -= 1
            j -= 1
        else:
            if matrix[i][j - 1] > matrix[i - 1][j]:
                j -= 1
            else:
                i -= 1
    if not A: return '-'
    return ''.join(A[::-1])


if __name__ == '__main__':
        
    s1 = 'abacaba'
    s2 = 'abcdcba'
    
    assert(LCS(s1, s2) == 'abcba')
