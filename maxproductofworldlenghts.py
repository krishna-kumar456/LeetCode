from collections import Counter

words = ["abcw","baz","foo","bar","xtfn","abcdef"]


d = {}
for w in words:
    mask = 0
    for c in set(w):
        mask |= (1 << (ord(c) - 97))
    d[mask] = max(d.get(mask, 0), len(w))
print(max([d[x] * d[y] for x in d for y in d if not x & y] or [0]))














# Steps

# 1. Iterate over list
# 2. Keep a variable for storing max product
# 3. Iterate another time for comparing with first item
# 4. Check if any letter exists between two items
# 5. If yes, then continue or else add max product between item lengths
# 6. If a new pair comes, compare product with max product


# def common(str1, str2):

#     # convert both strings into counter dictionary
#     dict1 = Counter(str1)
#     dict2 = Counter(str2)

#     # take intersection of these dictionaries
#     commonDict = dict1 & dict2

#     if len(commonDict) == 0:
#         return -1
#     else:
#         return 1


# max_product = 0

# for index, value in enumerate(i):
#     for i1, v2 in enumerate(i[index+1:]):
#         if common(value, v2) == 1:
#             continue
#         else:
#             if max_product is not 0:
#                 max_product = max(max_product, len(value) * len(v2))
#             else:
#                 max_product = len(value) * len(v2)


# print(max_product)
