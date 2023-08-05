#Problem Statment: Given the head of a singly linked list,
#reverse the list, and return the reversed list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
       self.val = val
       self.next = next
def reverseListIterative(head):
    prev = None
    curr = head
    while curr != None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

def reverseListRecursive(curr, prev = None):
    if curr == None:
        return prev
    next = curr.next
    curr.next = prev
    return reverseListRecursive(next, curr)

def printList(head):
    while head != None:
        print(head.val, end = ' ')
        head = head.next

head = None
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

printList(head)
print()
head = reverseListIterative(head)
printList(head)
print()
head = reverseListRecursive(head)
printList(head)