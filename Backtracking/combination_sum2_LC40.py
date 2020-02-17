class Solution():
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        def bcktrck(candidates, target, p):
            if target == 0:
                res.append(p)
                return
            for i in range(len(candidates)):
                if i > 0 and candidates[i] == candidates[i-1]:
                    continue
                elif candidates[i] > target:
                    break
                bcktrck(candidates[i+1:], target -
                        candidates[i], p + [candidates[i]])
        bcktrck(sorted(candidates), target, [])
        return res


if __name__ == '__main__':
    obj = Solution()
    candidates = [[2, 5, 2, 1, 2], [10, 1, 2, 7, 6, 1, 5]]
    target = [5, 8]
    ans = [
        [[1, 2, 2], [5]],
        [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
    ]

    for i in range(len(candidates)):
        assert(obj.combinationSum2(candidates[i], target[i]) == ans[i])
