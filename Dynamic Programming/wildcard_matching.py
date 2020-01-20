'''
Created on 11-Jan-2020

@author: Harsh
'''


class Solution(object):

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        matrix = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        
        matrix[0][0] = True
        
        i = 0
        while i < len(p) and p[i] == '*':
            matrix[0][i + 1] = True
            i += 1

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                    matrix[i][j] = matrix[i - 1][j - 1]
                elif p[j - 1] == '*':
                    matrix[i][j] = matrix[i - 1][j] or matrix[i][j - 1]
        
        return matrix[-1][-1]


if __name__ == '__main__':
    obj = Solution()
    S = ['aa', 'aa', 'cb', 'adceb', 'acdcb', 'adkfhsdjfbdsjp']
    P = ['*', 'a', '?a', '*a*b', 'a*c?b', 'a*p']
    ans = [True, False, False, True, False, True]
    for i in range(len(P)):
        assert(obj.isMatch(S[i], P[i]) == ans[i])
