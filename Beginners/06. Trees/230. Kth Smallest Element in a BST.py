#Problem statement: Given the root of a binary search tree, and an integer k, return the kth smallest value
#(1-indexed) of all the values of the nodes in the tree.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root, k):
    stack, inorder = [], []
    curr = root
    n = 0

    while curr != None:
        stack.append(curr)
        n += 1
        curr = curr.left

    while stack:
        curr = stack.pop()
        inorder.append(curr.val)
        if len(inorder) == k:
            return inorder[-1]
        if curr.right != None:
            curr = curr.right
            while curr != None:
                stack.append(curr)
                curr = curr.left

root = TreeNode(5)
root.left = TreeNode(3, TreeNode(2), TreeNode(4))
root.right = TreeNode(6, None, TreeNode(7))

print(kthSmallest(root, 2))