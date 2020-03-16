# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.cameras = 0

        def dfs(root):
            if not root:
                return 1
            left = dfs(root.left)
            right = dfs(root.right)
            if left == 0 or right == 0:
                self.cameras += 1
                # Current node needs a camera because
                # one of the child is not covered by any
                # camera
                return 2
            elif left == 2 or right == 2:
                # since one of the child has camera, current
                # node is covered
                return 1
            # default case current node is not covered
            return 0
        if dfs(root) == 0:
            return self.cameras + 1
        return self.cameras
