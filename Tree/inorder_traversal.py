# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def dfs(root, res):
            if not root:
                return
            dfs(root.left, res)
            res.append(root.val)
            dfs(root.right, res)
        res = []
        dfs(root, res)
        return res
