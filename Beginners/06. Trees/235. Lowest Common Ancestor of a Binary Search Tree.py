#Problem statment: Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes
#in the BST.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
def lowestCommonAncestor(root, p, q):
    if (p.val < root.val and q.val > root.val) or (p.val > root.val and q.val < root.val):
        return root
    elif p.val > root.val and q.val > root.val:
        return lowestCommonAncestor(root.right, p, q)
    elif p.val < root.val and q.val < root.val:
        return lowestCommonAncestor(root.left, p, q)
    elif (p.val == root.val) or (q.val == root.val):
        return root 