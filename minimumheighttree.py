from collections import defaultdict

n = 6
edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

count_dict = defaultdict(int)

for index, edge in enumerate(edges):
    count_dict[edge[0]]
    count_dict[edge[1]]

result = []

for k, v in count_dict.items():
    print(k, v)
    if v > 1:
        result.append(k)

print(result)