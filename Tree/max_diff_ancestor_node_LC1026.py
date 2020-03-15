# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Top to down
        def dfs(root, high, low):
            if not root:
                return high - low
            high = max(high, root.val)
            low = min(low, root.val)
            return max(dfs(root.left, high, low), dfs(root.right, high, low))
        return dfs(root, root.val, root.val)

        # Bottom up
        if not root or (not root.left and not root.right):
            return 0
        self.diff = float('-inf')

        def helper(root):
            if not root:
                return float('inf'), float('-inf')
            if not root.left and not root.right:
                return root.val, root.val
            lmn, lmx = helper(root.left)
            rmn, rmx = helper(root.right)
            lans = 0 if min(lmn, rmn) == float('inf') else min(lmn, rmn)
            rans = 0 if max(lmx, rmx) == float('-inf') else max(lmx, rmx)
            self.diff = max(self.diff, abs(root.val - lans),
                            abs(root.val - rans))
            return min(lmn, rmn, root.val), max(lmx, rmx, root.val)

        helper(root)
        return self.diff
