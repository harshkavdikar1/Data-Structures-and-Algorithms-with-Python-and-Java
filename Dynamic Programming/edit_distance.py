'''
Created on 11-Jan-2020

@author: Harsh
'''


class Solution(object):

    def minDistance(self, word1, word2):
        """
        LeetCode: 72
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word1: return len(word2)
        if not word2: return len(word1)
        A = list(range(len(word2) + 1))
        for i in range(1, len(word1) + 1):
            B = [i]
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    B.append(A[j - 1])
                else:
                    B.append(min(A[j], A[j - 1], B[j - 1]) + 1)
            A = B
        return A[-1]
    

if __name__ == '__main__':
    obj = Solution()
    w1 = ['horse', 'intention', 'zoologicoarchaeologist', '', 'a']
    w2 = ['ros', 'execution', 'zoogeologist', 'a', 'ab']
    ans = [3, 5, 10, 1, 1]
    for i in range(len(w1)):
        assert(obj.minDistance(w1[i], w2[i]) == ans[i])
        
