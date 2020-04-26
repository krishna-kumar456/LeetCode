class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

result = 0


def parse_tree(root, value):

    if root is None:
        return

    print(root.val)
    parse_tree(root.left, value * 10 + root.val)
    parse_tree(root.right, value * 10 + root.val)

    if root.left is None and root.right is None:
        result = value * 10 + root.val



t = TreeNode(4)
t.left = TreeNode(9)
t.left.left = TreeNode(5)
t.left.right = TreeNode(1)
t.right = TreeNode(0)

parse_tree(t, 0)
print(result)

