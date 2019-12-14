'''
Created on 14-Dec-2019

@author: Harsh
'''


class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        head = None
        while l1 and l2:
            sum = l1.val + l2.val + carry
            carry = sum / 10
            sum = sum % 10
            if head:
                head.next = ListNode(sum)
                head = head.next
            else:
                head = ListNode(sum)
                k = head
            l1 = l1.next
            l2 = l2.next
        if l1:
            while l1:
                sum = l1.val + carry
                carry = sum / 10
                sum = sum % 10
                head.next = ListNode(sum)
                l1 = l1.next
                head = head.next
        elif l2:
            while l2:
                print(head.val)
                sum = l2.val + carry
                carry = sum / 10
                sum = sum % 10
                head.next = ListNode(sum)
                l2 = l2.next
                head = head.next
        while carry != 0:
            val = carry % 10
            carry = carry / 10
            head.next = ListNode(val)
            head = head.next
            print(head.val)
        return k
