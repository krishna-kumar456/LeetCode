import copy

A = "bccaba"
B = "abacbc"


result = 0
seen = []

for item in list(A):
    if A == B:
        break
    else:
        a = A.index(item)
        b = B.index(item)

        if item in seen:
            del_B = copy.deepcopy(list(B))
            del_B.remove(item)
            b = del_B.index(item)

        if a == b:
            continue

        list_B = list(B)
        temp = list_B[a]
        list_B[a] = item
        list_B[b] = temp

        result += 1
        seen.append(item)

        B = ''.join(list_B)

print(result)
