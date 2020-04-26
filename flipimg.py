A = [[1,1,0],[1,0,1],[0,0,0]]

B = []
for item in A:
    B.append(item[::-1])


for item in B:
    for i,n in enumerate(item):
        if n == 1:
            item[i] = 0

        if n == 0:
            item[i] = 1

print(B)