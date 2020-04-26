class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



def mergeTree(t1, t2):
    if t1 and t2:
        t3 = TreeNode(t1.val + t2.val)
        t3.left = mergeTree(t1.left, t2.left)
        t3.right = mergeTree(t1.right, t2.right)
        return t3
    elif t1:
        return t1
    elif t2:
        return t2



def printt3(t3):
    if t3 is None:
        return

    print(t3.val)
    printt3(t3.left)
    printt3(t3.right)



t1 = TreeNode(1)
t1.left = TreeNode(3)
t1.right = TreeNode(2)
t1.left.left = TreeNode(5)

t2 = TreeNode(2)
t2.left = TreeNode(1)
t2.right = TreeNode(3)
t2.left.right = TreeNode(4)
t2.right.right = TreeNode(7)

t3 = mergeTree(t1, t2)

printt3(t3)



