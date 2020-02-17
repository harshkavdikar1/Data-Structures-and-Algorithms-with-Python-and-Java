class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def bcktrck(q, uppr_diag, lwr_diag, res):
            col = len(q)
            if col == n:
                res.append(1)
                return
            for row in range(n):
                if row not in q and row - col not in uppr_diag and row + col not in lwr_diag:
                    bcktrck(q + [row], uppr_diag + [row - col],
                            lwr_diag + [row+col], res)
        res = []
        bcktrck([], [], [], res)
        return sum(res)


if __name__ == '__main__':
    obj = Solution()
    nums = [4, 6, 8, 10]
    ans = [2, 4, 92, 724]

    for i in range(len(nums)):
        assert(obj.totalNQueens(nums[i]) == ans[i])