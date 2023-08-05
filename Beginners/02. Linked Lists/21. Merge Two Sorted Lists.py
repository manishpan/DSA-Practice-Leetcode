#Problem statement: You are given the heads of two sorted linked lists list1 and list2.

#Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first
#two lists.

#Return the head of the merged linked list.

class Node:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

def printList(head):
    while head != None:
        print(head.val, end = ' ')
        head = head.next

def mergeTwoLists(list1, list2):
    dummy = Node()
    tail = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    
    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2
    
    return dummy.next
    

head = None
list1 = Node(1)
list1.next = Node(2)
list1.next.next = Node(4)

list2 = Node(1)
list2.next = Node(3)
list2.next.next = Node(4)

print("List1: ")
printList(list1)
print()
print("List2: ")
printList(list2)
print()

printList(mergeTwoLists(list1, list2))