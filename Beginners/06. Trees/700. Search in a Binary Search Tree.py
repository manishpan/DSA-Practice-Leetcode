#problem statement: You are given the root of a binary search tree (BST) and an integer val.

#Find the node in the BST that the node's value equals val and return the subtree rooted with that node.
#If such a node does not exist, return null.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def searchBST(root, val):
    if not root:
        return None
    
    if root.val > val:
        return searchBST(root.left, val)
    elif root.val < val:
        return searchBST(root.right, val)
    else:
        return root
    
