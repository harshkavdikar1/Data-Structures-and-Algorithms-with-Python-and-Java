# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        def symmetric(left, right):
            if not left and not right:
                return True
            return left and right and left.val == right.val and symmetric(left.left, right.right) and symmetric(left.right, right.left)
        if symmetric(root.left, root.right): return True
        return False
