#Problem statement: You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

#Merge all the linked-lists into one sorted linked-list and return it.

def mergeKLists(lists):
    start = [0] * len(lists)
    end = [len(lists[x]) for x in range(len(lists))]

    res = []

    

lists = [[1,4,5], [1,3,4], [2,6]]
mergeKLists(lists)