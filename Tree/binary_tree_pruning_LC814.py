# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def dfs(root):
            if not root:
                return False

            left = dfs(root.left)
            if left is False:
                root.left = None

            right = dfs(root.right)
            if right is False:
                root.right = None
            return right or left or root.val == 1

        dfs(root)
        return root
