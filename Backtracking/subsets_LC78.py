class Solution():
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]

        def backtrack(nums, temp):
            for i in range(len(nums)):
                res.append(temp + [nums[i]])
                backtrack(nums[i+1:], temp + [nums[i]])
        backtrack(sorted(nums), [])
        return res


if __name__ == '__main__':
    obj = Solution()
    nums = [[1, 2, 3], [5, 7, 8, 6]]
    ans = [
        [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]],
        [[], [5], [5, 6], [5, 6, 7], [5, 6, 7, 8], [5, 6, 8], [5, 7], [
            5, 7, 8], [5, 8], [6], [6, 7], [6, 7, 8], [6, 8], [7], [7, 8], [8]]
    ]

    for i in range(len(nums)):
        assert(obj.subsets(nums[i]) == ans[i])
