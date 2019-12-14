'''
Created on 14-Dec-2019

@author: Harsh
'''


class Solution:

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        c1 = self.countItems(headA)
        c2 = self.countItems(headB)
        c3 = c1 - c2
        if c3 >= 0:
            while c3 != 0:
                headA = headA.next
                c3 -= 1
        else:
            while c3 != 0:
                headB = headB.next
                c3 += 1
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
    
    def countItems(self, head):
        count = 0
        while head:
            head = head.next
            count += 1
        return count
