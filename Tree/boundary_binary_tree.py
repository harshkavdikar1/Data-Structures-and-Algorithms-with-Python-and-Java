# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        if not root: return
        result = []
        def left_view(root):
            if not root.left and not root.right: return
            result.append(root.val)
            if root.left: left_view(root.left)
            else: left_view(root.right)
        
        def right_view(root):
            if not root.left and not root.right: return
            if root.right: right_view(root.right)
            else: right_view(root.left)
            result.append(root.val)
        
        def leaves(root):
            if not root: return
            if not root.left and not root.right:
                result.append(root.val)
                return
            leaves(root.left)
            leaves(root.right)
        
        
        result.append(root.val)
        if root.left:
            left_view(root.left)
            leaves(root.left)
        if root.right:
            leaves(root.right)
            right_view(root.right)
        
        return result