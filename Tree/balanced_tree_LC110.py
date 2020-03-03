# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def balanced(root):
            if not root:
                return True, 0
            l, lh = balanced(root.left)
            r, rh = balanced(root.right)
            return l and r and abs(rh-lh) < 2, max(lh, rh) + 1
        res, height = balanced(root)
        return res
