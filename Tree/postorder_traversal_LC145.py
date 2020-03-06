# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def dfs(root, res):
            if not root:
                return
            dfs(root.left, res)
            dfs(root.right, res)
            res.append(root.val)
        res = []
        dfs(root, res)
        return res

    def iterativePostorderTraversal(self, root):
        pass
