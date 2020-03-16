# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        Q = deque([root])
        res = []
        while Q:
            tempQ = deque()
            while Q:
                x = Q.popleft()
                if not x:
                    res.append("null")
                    continue
                res.append(str(x.val))
                tempQ.extend([x.left, x.right])
            Q = tempQ
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '':
            return
        res = deque(data.split(','))
        if not res[0]:
            return
        root = TreeNode(int(res.popleft()))
        Q = deque([root])
        while res and Q:
            x = res.popleft()
            node = Q.popleft()
            if x != "null":
                node.left = TreeNode(int(x))
                Q.append(node.left)
            if res:
                x = res.popleft()
                if x!='null':
                    node.right = TreeNode(int(x))
                    Q.append(node.right)
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
