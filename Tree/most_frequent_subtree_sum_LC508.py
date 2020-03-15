# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict


class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return
        res = defaultdict(int)

        def dfs(root):
            if not root:
                return 0
            s = root.val + dfs(root.left) + dfs(root.right)
            res[s] += 1
            return s
        dfs(root)
        t = max(res.values())
        return [x for x in res if res[x] == t]
