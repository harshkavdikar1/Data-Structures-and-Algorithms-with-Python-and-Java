'''
Created on 14-Dec-2019

@author: Harsh
'''


class Solution(object):

    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        root = head
        if head:
            head = self.flattensublist(head)
        return root
    
    def flattensublist(self, head):
        while head and (head.next or head.child):
            if head.child:
                tail = self.flattensublist(head.child)
                if head.next:
                    tail.next = head.next
                    head.next.prev = tail
                head.next = head.child
                head.child.prev = head
                head.child = None
                if tail.next:
                    head = tail.next
                else:
                    head = tail
            else:
                head = head.next
        return head
