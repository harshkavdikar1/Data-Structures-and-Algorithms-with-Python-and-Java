# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def dfs(root, res):
            if not root:
                return
            res.append(root.val)
            dfs(root.left, res)
            dfs(root.right, res)
        res = []
        dfs(root, res)
        return res

    def iterativePreorderTraversal(self, root):
        stack = []
        res = []
        while True:
            while root:
                res.append(root.val)
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop(-1)
            root = node.right
