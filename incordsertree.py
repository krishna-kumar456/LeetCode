class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

t = TreeNode(10)
t.left = TreeNode(5)
t.right = TreeNode(7)

stack = []

def traverseTree(t):
    if t == None:
        return

    stack.append(t.val)
    traverseTree(t.left)
    traverseTree(t.right)

traverseTree(t)

sorted_stack = sorted(stack, reverse=True)

t_new = TreeNode(sorted_stack.pop())

while sorted_stack:
    item = sorted_stack.pop()
    print(item)
    temp = TreeNode(item)
    t_new.right = temp
    t_new = t_new.right


def printtree(t):
    if t == None:
        return

    print(t.val)
    printtree(t.right)

printtree(t_new)