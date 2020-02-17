class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]

        res = []

        def bcktrck(nums, temp):
            if not nums:
                res.append(temp[:])
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                bcktrck(nums[:i] + nums[i+1:], temp + [nums[i]])
        bcktrck(sorted(nums), [])
        return res


if __name__ == '__main__':
    obj = Solution()
    nums = [[1, 1, 2], [3, 3, 0, 3]]
    ans = [
        [[1, 1, 2], [1, 2, 1], [2, 1, 1]],
        [[0, 3, 3, 3], [3, 0, 3, 3], [3, 3, 0, 3], [3, 3, 3, 0]]
    ]

    for i in range(len(nums)):
        assert(obj.permuteUnique(nums[i]) == ans[i])
