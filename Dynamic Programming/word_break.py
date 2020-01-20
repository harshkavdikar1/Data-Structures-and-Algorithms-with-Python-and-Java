'''
Created on 13-Jan-2020

@author: Harsh
'''

from collections import deque


class Solution(object):

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # DP solution
        wordDict = set(wordDict)
        A = [True] + [False] * len(s)
        for i in range(len(s) + 1):
            for j in range(i):
                if s[j:i] in wordDict and A[j] == True:
                    A[i] = True
                    break
        return A[-1]
        
        # BFS Solution
        Q = deque([0])
        v = set()
        while Q:
            index = Q.popleft()
            for i in range(index, len(s) + 1):
                if s[index:i] in wordDict and i not in v:
                    v.add(i)
                    Q.append(i)
                    if i == len(s): return True
        return False


if __name__ == '__main__':
    obj = Solution()
    s = ["leetcode", 'applepenapple', 'catsandog']
    word_dict = [["leet", "code"], ["apple", "pen"], ["cats", "dog", "sand", "and", "cat"]]
    ans = [True, True, False]
    for i in range(len(s)):
        assert(obj.wordBreak(s[i], word_dict[i]) == ans[i])
        
