'''
Created on 14-Dec-2019

@author: Hp-pc
'''


class ReverseLinkedList:

    def iterativeSolution(self, head):
        if head is None:
            return None

        prev = last = None
        curr = head
        while curr:
            last = curr.next
            curr.next = prev
            prev = curr
            curr = last
        head = prev
        return head

    def recursiveSolution(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head:
            return self.reverse(head)
        return None

    def reverse(self, head):
        if not head.next:
            return head
        tail = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return tail
