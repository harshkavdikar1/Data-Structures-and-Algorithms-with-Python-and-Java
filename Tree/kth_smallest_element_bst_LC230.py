# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.res = None

        def helper(root, k):
            if not root:
                return k
            k = helper(root.left, k)
            k -= 1
            if k == 0:
                self.res = root.val
                return 0
            k = helper(root.right, k)
            return k
        helper(root, k)
        return self.res
