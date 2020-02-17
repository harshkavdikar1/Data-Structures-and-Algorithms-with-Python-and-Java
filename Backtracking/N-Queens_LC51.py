class Solution():
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def bcktrck(q, uppr_diag, lwr_diag, res):
            col = len(q)
            if col == n:
                res.append(q)
                return
            for row in range(n):
                if row not in q and row - col not in uppr_diag and row + col not in lwr_diag:
                    bcktrck(q + [row], uppr_diag + [row - col],
                            lwr_diag + [row+col], res)
        res = []
        bcktrck([], [], [], res)
        return [['.'*row + 'Q' + '.'*(n-row-1) for row in s] for s in res]


if __name__ == '__main__':
    obj = Solution()
    nums = [4, 6]
    ans = [
        [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]],
        [[".Q....","...Q..",".....Q","Q.....","..Q...","....Q."],
        ["..Q...",".....Q",".Q....","....Q.","Q.....","...Q.."],
        ["...Q..","Q.....","....Q.",".Q....",".....Q","..Q..."],
        ["....Q.","..Q...","Q.....",".....Q","...Q..",".Q...."]]
    ]

    for i in range(len(nums)):
        assert(obj.solveNQueens(nums[i]) == ans[i])