'''
Created on 14-Dec-2019

@author: Harsh
'''


class Solution(object):

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tail = root = head
        while head and head.next:
            if head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                if head.val == root.val:
                    root = head.next
                head = head.next
                tail.next = head
            else:
                tail = head
                head = head.next
        return root
