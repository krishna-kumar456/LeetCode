left = 1
right = 22

result = []

for i in range(left, right + 1):
    temp = list(str(i))
    print("temp : ",temp)
    c = len(temp)
    d = 0

    for item in temp:
        print("item : ", item)
        if item is not '0':
            if i % int(item) == 0:
                d += 1

    if c == d:
        result.append(i)

print(result)
