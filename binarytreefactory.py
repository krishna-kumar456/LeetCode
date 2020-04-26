A = [2, 4, 5, 10]

A.sort()
dic = {num: 1 for num in A}
print(dic)
for i in range(1, len(A)):
    for j in range(i):
        q, res = divmod(A[i], A[j])
        print("q : " + str(q) + "  r : " + str(res))
        if res == 0 and q in dic:
            dic[A[i]] += dic[q] * dic[A[j]]

        print(dic)
print(sum(dic.values()) % (10 ** 9 + 7))