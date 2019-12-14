'''
Created on 14-Dec-2019

@author: Harsh
'''


class Solution:

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        last_tail = curr = head
        prev = last = last_head = None
        if k == 1 or not head:
            return head
        temp_count = k
        while curr:
            curr = curr.next
            temp_count -= 1
        if temp_count > 0:
            return head
        temp_count = k
        curr = head
        while curr:
            temp_count -= 1
            last = curr.next
            curr.next = prev
            prev = curr
            curr = last
            if temp_count == 0:
                temp_count = k
                if last_tail == head:
                    head = prev
                else:
                    last_tail.next = prev
                    last_tail = last_head
                last_head = curr
                prev = None
        if temp_count != 0:
            curr = prev
            prev = None
            while curr:
                last = curr.next
                curr.next = prev
                prev = curr
                curr = last
            last_tail.next = prev
        return head
