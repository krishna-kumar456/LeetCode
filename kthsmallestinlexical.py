n = 13
k = 2

arr = [x for x in range(1,n+1)]

print(arr)

for i, v in enumerate(arr):
    for j, v2 in enumerate(arr[i:]):

        if v2 / 10 == v:
            temp = arr[i+1]
            if temp / 10 == v:
                ones_v2 = v2 % 10
                ones_temp = temp % 10

                if ones_v2 > ones_temp:

                else:
                    pass

