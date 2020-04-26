from collections import Counter

nums = [2,2,1]

c = Counter(nums)

print(c)

for k,v in c.items():
    if v == 1:
        print(k)
