#Problem statement: Design your implementation of the linked list. You can choose to use a singly or
#doubly linked list.
#A node in a singly linked list should have two attributes: val and next. val is the value of the current node,
#and next is a pointer/reference to the next node.

#The following implementation is using doubly linked list
class MyLinkedList:

    class Node:
        def __init__(self, val):
            self.val = val
            self.next = None

    def __init__(self):
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        if index >= self.length:
            return -1
        count = 1
        curr = self.head
        while count < index-1:
            count += 1
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        temp = self.Node(val)
        temp.next = self.head
        self.head = temp
        self.length += 1

    def addAtTail(self, val: int) -> None:
        if self.length == 0:
            return self.addAtHead(val)
        curr = self.head
        while curr.next != None:
            curr = curr.next
        temp = self.Node(val)
        curr.next = temp
        self.length += 1
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            return self.addAtHead(val)
        if index <= self.length:
            count = 1
            curr = self.head
            while count < index:
                count += 1
                curr = curr.next
            temp = self.Node(val)
            temp.next = curr.next
            curr.next = temp
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        count = 1
        if index < self.length:
            while count < index - 1:
                count += 1
                curr = curr.next
            curr.val = curr.next.val
            curr.next = curr.next.next
            self.length -= 1