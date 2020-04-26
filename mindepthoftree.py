class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def min_depth(root):

    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1

    if root.left is None:
        return min_depth(root.right) + 1

    if root.right is None:
        return min_depth(root.left) + 1

    return min(min_depth(root.left), min_depth(root.right)) + 1


def level_order_min_depth(root):

    if root is None:
        return 0

    q = []

    q.append({'node': root, 'depth': 1})

    while(len(q) > 0):
        queueItem = q.pop(0)

        node = queueItem['node']
        depth = queueItem['depth']

        if node.left is None and node.right is None:
            return depth

        if node.left is not None:
            q.append({'node' : node.left, 'depth' : depth + 1})

        if node.right is not None:
            q.append({'node' : node.right, 'depth' : depth + 1})




root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print(level_order_min_depth(root))
