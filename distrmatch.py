S = "IDID"
# output = [0,4,1,3,2]

left = right = 0
res = [0]
for i in S:
    if i == "I":
        right += 1
        res.append(right)
    else:
        left -= 1
        res.append(left)

t = []

for i in res:
    t.append(i-left)

print([i - left for i in res])
print(t)

