# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if not s:
            return False
        return self.matches(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def matches(self, s, t):
        if not s and not t:
            return True
        return s and t and s.val == t.val and self.matches(s.left, t.left) and self.matches(s.right, t.right)
