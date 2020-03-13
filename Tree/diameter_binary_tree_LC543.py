# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        def helper(root):
            if not root:
                return 0, 0
            lh, lm = helper(root.left)
            rh, rm = helper(root.right)
            return max(lh, rh) + 1, max(lm, rm, lh + rh + 1)
        return helper(root)[1] - 1
