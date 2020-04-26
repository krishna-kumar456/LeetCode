s = "UD"

result = [0, 0]

for ch in s:
    print(ch)
    if ch == 'U':
        result[1] += 1
    elif ch == 'D':
        result[1] -= 1
    elif ch == 'L':
        result[0] -= 1
    elif ch == 'R':
        result[1] += 1



if result == [0, 0]:
    print(True)
else:
    print(False)

