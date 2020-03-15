# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.first = self.second = self.prev = None

        def helper(root):
            if not root:
                return

            helper(root.left)

            if not self.first and self.prev and self.prev.val >= root.val:
                self.first = self.prev
            if self.first and self.prev.val >= root.val:
                self.second = root

            self.prev = root

            helper(root.right)

        helper(root)

        self.first.val, self.second.val = self.second.val, self.first.val

        # Remove this statement while running it in leetcode
        return root