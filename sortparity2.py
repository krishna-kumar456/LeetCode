A = [4,2,5,7]

for i,v in enumerate(A):
    if i % 2 == 0:
        if v % 2 != 0:
            for j, v2 in enumerate(A[i+1:]):
                if j % 2 == 0:
                    A[i] = v2
                    A[j] = v
    elif i % 2 == 1:
        if v % 2 != 1:
            for j, v2 in enumerate(A[i+1:]):
                if j % 2 == 1:
                    A[i] = v2
                    A[j+1] = v


print(A)

