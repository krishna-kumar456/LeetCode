class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def invertSolver(t, temp):
    if t is None:
        return

    if temp is 0:
        temp = TreeNode(t.val)

    temp.left = t.right
    temp.right = t.left

    invertSolver(t.left, temp.left)
    invertSolver(t.right, temp.right)

    return temp


def invertTree(t):
    temp = 0
    return invertSolver(t, temp)



t = TreeNode(4)
t.left = TreeNode(2)
t.left.left = TreeNode(1)
t.left.right = TreeNode(3)
t.right = TreeNode(7)
t.right.left = TreeNode(6)
t.right.right = TreeNode (9)

#

def generateTreeList(r,temp):
    if r is None:
        return

    print(r.val)
    temp = TreeNode(r.val)

    generateTreeList(r.right, temp.right)
    generateTreeList(r.left, temp.left)




temp = None
t2 = generateTreeList(t, temp)

a = 1
print(a)