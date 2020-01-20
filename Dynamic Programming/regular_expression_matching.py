'''
Created on 11-Jan-2020

@author: Harsh
'''


class Solution(object):

    def isMatch(self, s, p):
        """
        Leetcode Problem : 10
        :type s: str
        :type p: str
        :rtype: bool
        """
        matrix = [[False for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        
        matrix[0][0] = True
        
        # Edge case check for patterns starting with 
        # a* or .* or a*a* for zero comparisons till we have
        # two continuous characters in p 
        for i in range(2, len(p) + 1):
            matrix[0][i] = matrix[0][i - 2] and p[i - 1] == '*'

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '.' or s[i - 1] == p[j - 1]:
                    matrix[i][j] = matrix[i - 1][j - 1]
                elif p[j - 1] == '*':
                    if p[j - 2] == '.' or s[i - 1] == p[j - 2]:
                        matrix[i][j] = matrix[i - 1][j] or matrix[i][j - 2]
                    else:
                        matrix[i][j] = matrix[i][j - 2] 
        return matrix[-1][-1]

        
if __name__ == '__main__':
    obj = Solution()
    S = ['aab', 'mississippi', 'ab', 'aa', 'aa', 'ab',
         "aasdfasdfasdfasdfas", "aaa"]
    P = ['c*a*b', 'mis*is*p*.', '.', 'a*', 'a', '.*',
         "aasdf.*asdf.*asdf.*asdf.*s", "ab*a*c*a"]
    ans = [True, False, False, True, False, True, True, True]
    for i in range(len(P)):
        assert(obj.isMatch(S[i], P[i]) == ans[i])
