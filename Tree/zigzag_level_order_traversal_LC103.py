from collections import deque

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return

        Q = deque([root])
        res = []
        flag = True
        while Q:
            temp_q = deque()
            temp = []
            while Q:
                x = Q.popleft()
                if x.left:
                    temp_q.append(x.left)
                if x.right:
                    temp_q.append(x.right)
                temp.append(x.val)
            if flag is False:
                temp.reverse()
            res.append(temp)
            flag = not flag
            Q = temp_q
        return res
