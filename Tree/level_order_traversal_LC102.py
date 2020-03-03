from collections import deque

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return
        Q = deque([root])
        res = []
        while Q:
            temp_queue = deque()
            temp = []
            while Q:
                x = Q.popleft()
                if x.left:
                    temp_queue.append(x.left)
                if x.right:
                    temp_queue.append(x.right)
                temp.append(x.val)
            Q = temp_queue
            res.append(temp)
        return res
