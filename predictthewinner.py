n = [1,567,1,1]

sum_a = 0
sum_b = 0

for i, v in enumerate(n):

    if len(n) == 2:
        sum_b = max(n)
    else:
        if i % 2 == 1:
            sum_a += v
        elif i % 2 == 0:
            sum_b += v

if sum_a > sum_b:
    print(False)

else:
    print(True)