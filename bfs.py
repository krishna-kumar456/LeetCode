from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, k, v):
        self.graph[k].append(v)

    def bfs(self, s):

        visited = [False] * len(self.graph)

        queue = []

        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.pop(0)
            print(s, sep=" ")

            for i in self.graph[s]:

                if visited[i] is False:
                    queue.append(i)
                    visited[i] = True



g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.bfs(0)
