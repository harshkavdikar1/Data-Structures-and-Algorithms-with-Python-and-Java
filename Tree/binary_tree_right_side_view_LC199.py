# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return
        res = []
        Q = deque([root])

        while Q:
            temp = deque()
            x = None
            while Q:
                x = Q.popleft()
                if x.left:
                    temp.append(x.left)
                if x.right:
                    temp.append(x.right)
            if x:
                res.append(x.val)
            Q = temp

        return res
