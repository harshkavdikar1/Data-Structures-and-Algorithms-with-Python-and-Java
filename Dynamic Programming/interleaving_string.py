'''
Created on 11-Jan-2020

@author: Harsh
'''


class Solution(object):

    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if not s1: return s2 == s3
        if not s2: return s1 == s3
        
        if len(s3) != len(s2) + len(s1): return False
        
        matrix = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        
        matrix[0][0] = True
        
        for i in range(len(s1) + 1):
            a = s1[i - 1] if i > 0 else ''
            for j in range(len(s2) + 1):
                if i == 0 and j == 0: continue
                b = s2[j - 1] if j > 0 else ''
                c = s3[i + j - 1]
                matrix[i][j] = (c == a and matrix[i - 1][j]) or (b == c and matrix[i][j - 1])
        return matrix[-1][-1]


if __name__ == '__main__':
    obj = Solution()
    s1 = ['aabcc', 'aabcc']
    s2 = ['dbbca', 'dbbca']
    s3 = ['aadbbcbcac', 'aadbbbaccc']
    ans = [True, False]
    for i in range(len(s1)):
        assert(obj.isInterleave(s1[i], s2[i], s3[i]) == ans[i])
