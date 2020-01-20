'''
Created on 12-Jan-2020

@author: Harsh
'''

from collections import deque

class Solution(object):

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # DP
        dp = [0] + [float('inf')] * (amount)
        
        for coin in coins:
            for j in range(coin, amount + 1):
                dp[j] = min(dp[j - coin] + 1, dp[j])
        return -1 if dp[amount] == float('inf') else dp[amount]
    
        # BFS
        if amount == 0: return 0
        Q = deque([0])
        v = set()
        val = 0
        while Q:
            new_Q = deque()
            val += 1
            while Q:
                x = Q.popleft()
                for coin in coins:
                    if coin + x not in v and coin + x <= amount:
                        if coin + x == amount:
                            return val
                        v.add(coin + x)
                        new_Q.append(coin + x)
            Q = new_Q
        return -1


if __name__ == '__main__':
    obj = Solution()
    coins = [[2], [1, 2, 5], [2, 5], [399, 313, 460, 317, 401, 173, 116, 17, 121]]
    amount = [3, 11, 11, 7335]
    ans = [-1, 3, 4, 18]

    for i in range(len(coins)):
        assert(obj.coinChange(coins[i], amount[i]) == ans[i])
