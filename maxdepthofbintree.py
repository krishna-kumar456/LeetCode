class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def maxDepth(root):

    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1

    if root.left is None:
        return maxDepth(root.right) + 1

    if root.right is None:
        return maxDepth(root.left) + 1

    return max(maxDepth(root.left), maxDepth(root.right)) + 1



t = TreeNode(3)
t.left = TreeNode(9)
t.right = TreeNode(20)
t.right.left = TreeNode(15)
t.right.right = TreeNode(7)


print(maxDepth(t))