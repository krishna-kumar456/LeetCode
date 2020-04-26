n = 5

result = []

for i, v in enumerate(range(1, n+1)):
    if v == 1:
        result.append([1])

    if i == 1:
        result.append([1,1])

    if i > 1:
        temp = []
        for i2 in range(i):
            if i2 == 0 or i2 == i:
                temp.append(1)

            else:
                prevArray = result[i - 1]
                if i2 - 1 >= 0:
                    calc_val = sum( prevArray[i2-1:i2+1])
                else:
                    calc_val = prevArray[i2]

                temp.append(calc_val)
        temp.append(1)

        result.append(temp)

