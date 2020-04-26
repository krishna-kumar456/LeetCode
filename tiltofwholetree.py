class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def preorder_traversal(root, tilt):
    if root is None:
        return 0

    preorder_traversal(root.left, tilt)
    preorder_traversal(root.right, tilt)

    if root.left is None:
        tilt = tilt + 0

    if root.right is None:
        tilt = tilt + 0

    if root.left is not None and root.right is not None:
        tilt = tilt + abs(root.left.val - root.right.val)

    return tilt

tree = TreeNode(1)
tree.left = TreeNode(2)

print(preorder_traversal(tree, 0))