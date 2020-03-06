# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        def dfs(root):
            temp = None
            if root.left:
                temp = root.right
                root.right = root.left
                new_rp = dfs(root.left)
                root.left = None
                new_rp.right = temp
                if temp:
                    return dfs(temp)
                return new_rp
            elif root.right:
                return dfs(root.right)
            return root
        dfs(root)
        return root
