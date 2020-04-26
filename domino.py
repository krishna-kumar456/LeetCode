A = [1,2,1,1,1,2,2,2]
B = [2,1,2,2,2,2,2,2]


max_occ_A = max ( set ( A ), key = A.count)
max_occ_B = max ( set ( B ), key = B.count)

max_occ = max (max_occ_A, max_occ_B)


print("max_occ_A" + str(max_occ_A))
print("max_occ_B" + str(max_occ_B))

non_max_occ_A = [x for x in A if x != max_occ]
non_max_occ_B = [x for x in B if x != max_occ]

print("non_max_occ_A" + str(non_max_occ_A))
print("non_max_occ_B" + str(non_max_occ_B))

min_swaps_A = 0
min_swaps_B = 0

for i, v in enumerate(non_max_occ_A):
    print("B[A.index(v)] : " + str(B[A.index(v)]))
    if B[A.index(v)] == max_occ:
        min_swaps_A += 1
        A[A.index(v)] = max_occ
        print("min_swaps_A : " + str(min_swaps_A))

for i, v in enumerate(non_max_occ_B):
    print("A[B.index(v)] : " + str(A[B.index(v)]))
    if A[B.index(v)] == max_occ:
        min_swaps_B += 1
        B[B.index(v)] = max_occ

        print("min_swaps_B : " + str(min_swaps_B))



if len(list(set(A))) == 1 or len(list(set(B))) == 1 :
    print(min(min_swaps_A, min_swaps_B))
else:
    print("-1")

