class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums: return [[]]
        
        res = []
        
        def bcktrck(nums, temp):

            if not nums:
                res.append(temp[:])
                return

            for i in range(len(nums)):
                bcktrck(nums[:i] + nums[i+1:], temp + [nums[i]])

        bcktrck(nums, [])
        return res


if __name__ == '__main__':
    obj = Solution()
    nums = [[1,2,3], [1,6,8,9]]
    ans = [
        [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]],
        [[1,6,8,9],[1,6,9,8],[1,8,6,9],[1,8,9,6],[1,9,6,8],
            [1,9,8,6],[6,1,8,9],[6,1,9,8],[6,8,1,9],[6,8,9,1],[6,9,1,8],
            [6,9,8,1],[8,1,6,9],[8,1,9,6],[8,6,1,9],[8,6,9,1],[8,9,1,6],
            [8,9,6,1],[9,1,6,8],[9,1,8,6],[9,6,1,8],[9,6,8,1],[9,8,1,6],
            [9,8,6,1]]
    ]

    for i in range(len(nums)):
        assert(obj.permute(nums[i]) == ans[i])
