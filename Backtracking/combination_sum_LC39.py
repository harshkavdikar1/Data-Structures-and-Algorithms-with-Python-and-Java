class Solution():
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        def bckrtrck(candidates, target, arr):
            if target == 0:
                res.append(arr)
            for i in range(len(candidates)):
                if candidates[i] > target:
                    break
                bckrtrck(candidates[i:], target -
                         candidates[i], arr + [candidates[i]])
        bckrtrck(sorted(candidates), target, [])
        return res


if __name__ == '__main__':
    obj = Solution()
    candidates = [[2, 3, 6, 7], [2, 3, 5]]
    target = [7, 8]
    ans = [
        [[2, 2, 3], [7]],
        [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    ]

    for i in range(len(candidates)):
        assert(obj.combinationSum(candidates[i], target[i]) == ans[i])
