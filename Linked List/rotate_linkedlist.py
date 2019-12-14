'''
Created on 14-Dec-2019

@author: Harsh
'''


class Solution:

    def rotateRight(self, head, k):
        tail = root = head
        if head is None or k == 0:
            return head
        length = 0
        while root:
            length += 1
            root = root.next
        k = k % length
        root = head
        while root:
            if k == 0:
                while root.next:
                    root = root.next
                    tail = tail.next
                root.next = head
                head = tail.next
                tail.next = None
                return head
            root = root.next
            k -= 1
        return head

    def rotateLeft(self, head, k):
        tail = root = head
        if head is None or k == 0:
            return head
        while root.next:
            k -= 1
            if k == 0:
                tail = root
                while root.next:
                    root = root.next
                root.next = head
                head = tail.next
                tail.next = None
                return head
            root = root.next
        return head
