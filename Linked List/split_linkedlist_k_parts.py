'''
Created on 14-Dec-2019

@author: Harsh
'''


class Solution(object):

    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        output = []
        head = root
        length = 0
        while head:
            head, length = head.next, length + 1
        head = root
        parts = length % k
        length = length / k
        if length == 0:
            while head:
                curr, curr.next, head = head, None, head.next
                output.append(curr)
        else:
            while k > 0:
                t = length
                curr = head
                if parts > 0:
                    t += 1
                while head:
                    t -= 1
                    if t == 0:
                        head.next, head = None, head.next
                        break
                    head = head.next
                parts -= 1
                k -= 1
                output.append(curr)
        for _ in range(len(output), k):
            output.append(None)
        return output
