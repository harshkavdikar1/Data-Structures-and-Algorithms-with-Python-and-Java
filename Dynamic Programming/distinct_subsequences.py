'''
Created on 11-Jan-2020

@author: Harsh
'''


class Solution(object):

    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        T = [1] + [0] * len(t)
        
        for i in range(1, len(s) + 1):
            A = [1] + [0] * len(t)
            for j in range(1, len(t) + 1):
                A[j] = T[j]
                if s[i - 1] == t[j - 1]:
                    A[j] += T[j - 1]
            T = A
        return T[-1]


if __name__ == '__main__':
    obj = Solution()
    
    s = ['rabbbit', 'babgbag', 'abss', '']
    t = ['rabbit', 'bag', '', 'abyss']
    ans = [3, 5, 1, 0]
    
    for i in range(len(s)):
        assert(obj.numDistinct(s[i], t[i]) == ans[i])
