# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, s):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def dfs(root, s, curr_path, res):
            if not root:
                return

            s -= root.val

            if root.left is None and root.right is None and s == 0:
                res.append(curr_path + [root.val])
                return

            dfs(root.left, s, curr_path + [root.val], res)
            dfs(root.right, s, curr_path + [root.val], res)

        res = []
        dfs(root, s, [], res)
        return res
