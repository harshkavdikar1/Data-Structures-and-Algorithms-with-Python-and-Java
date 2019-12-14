'''
Created on 14-Dec-2019

@author: Harsh
'''

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        slow = head
        while slow and fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
