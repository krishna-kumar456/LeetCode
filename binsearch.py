b = [8,5,1,7,10,12]


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


root = TreeNode(b[0])

stack = [root] # , 5 , 1

for value in b[1:]:
    print(value)
    if value < stack[-1].val:
        stack[-1].left = TreeNode(value)
        stack.append(stack[-1].left)

    else:
        while stack and stack[-1].val < value:
            last = stack.pop()

        last.right = TreeNode(value)
        stack.append(last.right)

