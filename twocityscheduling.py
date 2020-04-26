costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]

n = len(costs) // 2
a_count = 0
b_count = 0
result = 0

for item in costs:
    if item[0] < item[1]:
        if a_count < n:
            a_count += 1
            result += item[0]
        else:
            if b_count < n:
                b_count += 1
                result += item[1]

    else:
        if b_count < n:
            b_count += 1
            result += item[1]
        else:
            if a_count < n:
                a_count += 1
                result += item[0]

print(a_count)
print(b_count)


print(result)