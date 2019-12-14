'''
Created on 14-Dec-2019

@author: Harsh
'''


class Solution(object):

    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        detected_node = self.detectLoop(head)
        if detected_node:
            while head != detected_node:
                head = head.next
                detected_node = detected_node.next
            return detected_node
        return None
        
    def detectLoop(self, head):
        slow = head
        fast = head
        while fast and slow and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return fast
            if fast == None:
                return None
        return None
