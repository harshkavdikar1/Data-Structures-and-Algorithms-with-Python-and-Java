'''
Created on 13-Jan-2020

@author: Harsh
'''

# from collections import deque


class Solution(object):

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        # BFS - Timeout
#         Ans = []
#         
#         Q = deque([[0, '']])
#         v = set()
#         
#         while Q:
#             # print Q
#             index, word = Q.popleft() 
#             for i in range(index, len(s) + 1):
#                 if s[index: i] in wordDict:
#                     w = word + ' ' + s[index:i]
#                     if (i, w) not in v:
#                         v.add((i, w))
#                         Q.append([i, w])
#                         if i == len(s):
#                             Ans.append(w.lstrip())
#         return Ans
    
        # Backtracking
        Ans = []
        
        def dfs(s, Ans, wordDict, word):
            if not self.check(s, wordDict): return
            for j in range(len(s) + 1):
                if s[:j] in wordDict:
                    if j == len(s):
                        Ans.append((word + s).lstrip())
                    else:
                        dfs(s[j:], Ans, wordDict, word + s[:j] + ' ')

        dfs(s, Ans, set(wordDict), '')
        return Ans

    def check(self, s, dic):
        dp = [False for i in range(len(s) + 1)]
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in dic:
                    dp[i] = True
        return dp[-1]

    
if __name__ == '__main__':
    obj = Solution()
    s = ["catsandog", 'pineapplepenapple', 'catsanddog']
    word_dict = [["cats", "dog", "sand", "and", "cat"],
                 ["apple", "pen", "applepen", "pine", "pineapple"],
                 ["cats", "dog", "sand", "and", "cat"]]
    ans = [[], ["pine apple pen apple", "pine applepen apple", "pineapple pen apple"],
           ["cat sand dog", "cats and dog"]]
    for i in range(len(s)):
        assert(obj.wordBreak(s[i], word_dict[i]) == ans[i])
        
