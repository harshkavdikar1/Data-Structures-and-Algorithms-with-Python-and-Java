'''
Created on 14-Dec-2019

@author: Harsh
'''


class Node(object):

    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution(object):

    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head: return
        newList = self.createnewList(head).next
        pnew = newList
        curr = head    
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        pold = head        
        while pold:
            pold.next = pnew.next
            pold = pold.next
            if pold:
                pnew.next = pold.next
            else:
                pnew.next = None
            pnew = pnew.next
        return newList

    def createnewList(self, head):
        root = head
        while head:
            cur = Node(head.val, None, None)
            cur.next = head.next
            head.next = cur
            head = cur.next
        return root
