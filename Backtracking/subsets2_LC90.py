class Solution():
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]

        def backtrack(nums, temp):
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                res.append(temp + [nums[i]])
                backtrack(nums[i+1:], temp + [nums[i]])
        backtrack(sorted(nums), [])
        return res


if __name__ == '__main__':
    obj = Solution()
    nums = [[1, 2, 2], [3, 3, 0, 3]]
    ans = [
        [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]],
        [[], [0], [0, 3], [0, 3, 3], [0, 3, 3, 3], [3], [3, 3], [3, 3, 3]]
    ]

    for i in range(len(nums)):
        assert(obj.subsetsWithDup(nums[i]) == ans[i])
