# Not complete
n = 2
m = 3

indices = [[0,1],[1,1]]

mat = [[0 for _ in range(m)] for _ in range(n)]

for item in indices:
    mat[item[0]] = [x+1 for x in mat[item[0]]]
    mat[item[1]] =  [x+1 for x in mat[item[1]]]

count_odd = 0

for item in mat:
    for i in item:
        if i % 2 == 1:
            count_odd += 1

print(count_odd)
