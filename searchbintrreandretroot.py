class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



def searchBST(root, val):
    if root and root.val != val:
        return searchBST(root.left, val) if val < root.val else searchBST(root.right, val)
    return root

t = TreeNode(4)
t.left = TreeNode(2)
t.left.left = TreeNode(1)
t.left.right = TreeNode(3)
t.right = TreeNode(7)


print(searchBST(t, 2))