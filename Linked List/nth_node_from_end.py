'''
Created on 14-Dec-2019

@author: Hp-pc
'''


class Solution(object):

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        tail = root = head
        while root:
            n -= 1
            if n == 0:
                if root.next:
                    while root.next.next:
                        root = root.next
                        tail = tail.next
                elif tail == head:
                    head = head.next
                    return head
                tail.next = tail.next.next
                return head
            root = root.next
        return head
