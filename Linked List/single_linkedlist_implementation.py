'''
Created on 14-Dec-2019

@author: Harsh
'''

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        head = self.root
        while head:
            if index==0:
                return head.val
            index-=1
            head = head.next
        return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if self.root:
            x = ListNode(val)
            x.next = self.root
            self.root = x
        else:
            self.root = ListNode(val)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        head = self.root
        while head.next:
            head = head.next
        head.next = ListNode(val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        head = self.root
        if index == 0:
            self.addAtHead(val)
        else:
            while head:
                index-=1
                if index==0:
                    node = ListNode(val)
                    node.next = head.next
                    head.next = node
                    break
                head = head.next

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        head = self.root
        while head:
            index-=1
            if index==0:
                try:
                    head.next = head.next.next
                except AttributeError:
                    head.next = None
                break
            head = head.next

    def printLL(self):
        """
        print all the Linked List Elements
        """
        head = self.root
        while head:
            print(head.val)
            head = head.next


if __name__ == "__main__":
    # Your MyLinkedList object will be instantiated and called as such:
    obj = MyLinkedList()
    param_1 = obj.get(1)
    obj.addAtHead(1)
    obj.addAtTail(3)
    obj.addAtIndex(1,2)
    param_1 = obj.get(1)
    obj.deleteAtIndex(1)
    param_1 = obj.get(1)
    obj.printLL()