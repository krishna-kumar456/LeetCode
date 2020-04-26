 def iterative_bfs(self, root):
        if not root: return 0
        stack = [root]
        out = 0
        while len(stack):
            temp = []
            while len(stack):
                ele = stack.pop()
                for node in ele.children:
                    temp.append(node)
            stack = temp
            out += 1

        return out


def iterative_dfs(self, root):
    if not root: return 0
    stack = [[root, 0]]
    out = 1
    while len(stack):
        top, level = stack.pop()
        for node in top.children:
            stack.append([node, level + 1])
        out = max(out, 1 + level)
    return out

def recursive(self, root):
    def rec(root):
        if root:
            curr = 1
            for node in root.children:
                curr = max(curr, 1 + rec(node))
            return curr
        return 0
    return rec(root)