class Solution():
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []

        def backtrack(k, n, low, temp, sm, res):
            if k == 0:
                if sm == n:
                    res.append(temp)
                return
            for i in range(low, 10):
                if sm + i > n:
                    break
                backtrack(k-1, n, i+1, temp + [i], sm+i, res)
        backtrack(k, n, 1, [], 0, res)
        return res


if __name__ == '__main__':
    obj = Solution()
    k = [3, 3]
    n = [9, 10]
    ans = [
        [[1, 2, 6], [1, 3, 5], [2, 3, 4]],
        [[1, 2, 7], [1, 3, 6], [1, 4, 5], [2, 3, 5]]
    ]

    for i in range(len(k)):
        assert(obj.combinationSum3(k[i], n[i]) == ans[i])
