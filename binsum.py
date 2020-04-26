root = [10,5,15,3,7,None,18]
L = 7
R = 15

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def generateTreeList(r, result):
    if r is None:
        return

    result.append(r.val)
    generateTreeList(r.left, result)
    generateTreeList(r.right, result)


    return result

result = []

t = TreeNode(10)
t.left = TreeNode(5)
t.right = TreeNode(7)

generateTreeList(t, result)



for index, item in enumerate(root):
    if item == None:
        root[index] = 0

print(sorted(root))

summ = 0

for item in sorted(root):
    if item >= L and item <=R:
        summ+= item

print(summ)