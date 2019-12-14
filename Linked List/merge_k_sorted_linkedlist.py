'''
Created on 14-Dec-2019

@author: Harsh
'''


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        l = 0
        h = len(lists)
        if h == 0:
            return None
        elif h == 1:
            return lists[0]
        k = self.merge(lists, l, h - 1)
        return k
    
    def merge(self, lists, l, h):
        if h - l == 1:
            return self.mergeTwoLists(lists[l], lists[h])
        elif l == h:
            return lists[l]
        m = l + (h - l) / 2
        a = self.merge(lists, l, m)
        b = self.merge(lists, m + 1, h)
        return self.mergeTwoLists(a, b)
        
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(None)
        head = l3
        while l1 and l2:
            if l1.val > l2.val:
                l3.next = l2
                l2 = l2.next
            else:
                l3.next = l1
                l1 = l1.next
            l3 = l3.next
        
        if l1:
            l3.next = l1
        elif l2:
            l3.next = l2
        
        return head.next
