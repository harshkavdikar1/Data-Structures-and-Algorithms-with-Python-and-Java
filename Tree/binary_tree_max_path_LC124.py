# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = float('-inf')

        def dfs(root):
            if not root:
                return 0
            leftPath = dfs(root.left)
            rightPath = dfs(root.right)
            self.res = max(self.res, leftPath + rightPath + root.val)
            return max(max(leftPath, rightPath) + root.val, 0)
        dfs(root)
        return self.res
