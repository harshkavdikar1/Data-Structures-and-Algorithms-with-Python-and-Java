# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root, lp=float('inf'), rp=float('-inf')):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if root.left and (root.left.val >= root.val or root.left.val <= rp):
            return False
        if root.right and (root.right.val <= root.val or root.right.val >= lp):
            return False
        return self.isValidBST(root.left, root.val, rp) and self.isValidBST(root.right, lp,  root.val)
