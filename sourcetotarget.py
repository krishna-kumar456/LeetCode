graph = [[1, 2], [3], [3], []]

N = len(graph)

def solve(node):
    print("node : " + str(node))
    if node == N-1: return [[N-1]]
    ans = []
    for nei in graph[node]:
        print("nei : " + str(nei))
        for path in solve(nei):
            print("path : " + str(path))
            ans.append([node] + path)
    return ans

print(solve(0))