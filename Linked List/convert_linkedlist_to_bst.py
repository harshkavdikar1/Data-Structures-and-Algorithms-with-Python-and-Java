'''
Created on 14-Dec-2019

@author: Harsh
'''


class ListNode(object):
    """
    Definition for singly-linked list.
    """

    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode(object):
    """
    Definition for a binary tree node.
    """

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head: return
        elif not head.next: return TreeNode(head.val)
        fast = head.next
        slow = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        if fast.next:
            fast = fast.next
        root = TreeNode(slow.next.val)
        right = slow.next.next
        slow.next = None
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(right)
        return root    
