'''
Created on 14-Dec-2019

@author: Harsh
'''


class Solution(object):

    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head:
            return self.swap(head, head.next)
        
    def swap(self, head, tail):
        if not tail: return head
        if tail.next:
            head.next = self.swap(tail.next, tail.next.next)
        else:
            head.next = None
        tail.next = head
        return tail
