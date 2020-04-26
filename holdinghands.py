row = [0, 2, 4, 1, 3, 5]



min_swaps = 0

for i, v in enumerate(row):
    if v % 2 == 0:
        pos_pair = row.index(v + 1)

    elif v % 2 == 1:
        pos_pair = row.index(v - 1)

    if abs(pos_pair - i) == 1:
        continue
    else:
        row[i+1], row[pos_pair] = row[pos_pair], row[i+1]
        min_swaps += 1

print(min_swaps)
