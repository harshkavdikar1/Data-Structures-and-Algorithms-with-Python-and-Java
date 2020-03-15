# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        Q = deque([root])
        while Q:
            tempQ = deque()
            while Q:
                x = Q.popleft()
                if x.left:
                    tempQ.append(x.left)
                else:
                    if x.right:
                        return False
                    Q.extend(tempQ)
                    return self.checkForComleteness(Q)
                if x.right:
                    tempQ.append(x.right)
                else:
                    Q.extend(tempQ)
                    return self.checkForComleteness(Q)
            Q = tempQ
        return True

    def checkForComleteness(self, Q):
        while Q:
            x = Q.popleft()
            if x.left or x.right:
                return False
        return True
