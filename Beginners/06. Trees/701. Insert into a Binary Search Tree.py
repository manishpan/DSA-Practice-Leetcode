#Problem statement: You are given the root node of a binary search tree (BST) and a value to insert into the tree.
#Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the
#original BST.

#Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after
#insertion. You can return any of them.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insertIntoBST(root, val):
    curr = root
    temp = TreeNode(val)

    if not curr:
        return temp
    
    while True:
        if curr.val < val:
            if not curr.right:
                break
            curr = curr.right
        else:
            if not curr.left:
                break
            curr = curr.left
    
    if curr.val < val:
        curr.right = temp
    else:
        curr.left = temp
    return root