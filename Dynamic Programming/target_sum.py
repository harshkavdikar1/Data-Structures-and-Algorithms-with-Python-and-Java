'''
Created on 13-Jan-2020

@author: Harsh
'''

from collections import defaultdict


class Solution(object):

    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if not nums: return 0
        dp = {nums[0]: 1, -nums[0]: 1} if nums[0] != 0 else {0: 2}
        for i in range(1, len(nums)):
            tdp = defaultdict(int)
            for val in dp:
                tdp[val + nums[i]] += dp[val]
                tdp[val - nums[i]] += dp[val]
            dp = tdp
        return dp.get(S, 0)


if __name__ == '__main__':
    obj = Solution()
    nums = [[0,0,0,0,0,0,0,0,1], [1], [1, 1, 1, 1, 1]]
    S = [1, 2, 3]
    ans = [256, 0, 5]

    for i in range(len(nums)):
        assert(obj.findTargetSumWays(nums[i], S[i]) == ans[i])    

