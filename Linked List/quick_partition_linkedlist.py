'''
Created on 14-Dec-2019

@author: Harsh
'''


class Solution(object):

    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        root = head
        left = right = None
        if head and head.next:
            if head.val >= x:
                right = head
            else:
                left = head
            while head.next:
                if head.next.val < x:
                    if left is None:
                        left = head.next
                        root = left
                    else:
                        left.next = head.next
                        left = left.next
                    if right is not None:
                        head.next = head.next.next
                    else:
                        head = head.next
                elif right is None:
                    right = head.next
                    head = head.next
                    print(right.val)
                else:
                    head = head.next
            if left:
                left.next = right
        return root
