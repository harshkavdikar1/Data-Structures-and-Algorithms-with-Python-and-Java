# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution(object):

    # Runtime = O(N)
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        res = 0
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
                res += 1
            Q = temp
        return res

    # Runtime = O(logn*logn)
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        def getDepth(root):
            if not root:
                return 0
            x = 1
            while root.left:
                x += 1
                root = root.left
            return x

        leftDepth = getDepth(root.left)
        rightDepth = getDepth(root.right)
        if leftDepth == rightDepth:
            return 2**leftDepth + self.countNodes(root.right)
        else:
            return 2**rightDepth + self.countNodes(root.left)
