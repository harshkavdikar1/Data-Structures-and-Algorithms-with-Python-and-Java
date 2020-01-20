'''
Created on 13-Jan-2020

@author: Harsh
'''


class Solution(object):

    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [1] + [0] * (amount)
        
        for num in coins:
            for i in range(num, amount + 1):
                dp[i] += dp[i - num]
        return dp[amount]

