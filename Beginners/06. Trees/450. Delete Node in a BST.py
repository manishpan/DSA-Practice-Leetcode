#problem Statement: Given a root node reference of a BST and a key, delete the node with the given key in the BST.
#Return the root node reference (possibly updated) of the BST.

#Basically, the deletion can be divided into two stages:

#Search for a node to remove.
#If the node is found, delete the node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def getInorderSuccessor(curr):
    while not curr.left:
        curr = curr.left
    return curr.key

def deleteNode(root, key):
    if not root:
        return
    if root.val > key:
        root.left = deleteNode(root.left, key)
    elif root.val < key:
        root.right = deleteNode(root.right, key)
    else:
        if root.left == None:
            return root.right
        elif root.right == None:
            return root.left
        else:
            succ = getInorderSuccessor(root.right)
            root.key = succ
            root.right = deleteNode(root.right, succ)
    return root
    
