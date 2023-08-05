#Problem Statement: Given the root of a binary tree, return the inorder traversal of its nodes' values.

def InorderTraversal(root):
    inorder, stack = [], []
    curr = root

    while curr != None:
        stack.append(curr)
        curr = curr.left

    while stack:
        curr = stack.pop()
        inorder.append(curr.val)
        if curr.right != None:
            curr = curr.right
            while curr != None:
                stack.append(curr)
                curr = curr.left
    
    return inorder