from itertools import combinations

def check_similar(A, B):
    comparison = False

    for item in B:
        if sorted(A) == sorted(item):
            comparison = True

    return comparison

nums = [-5,5,4,-3,0,0,4,-2]
# com_nums = combinations_with_replacement(nums, 4)
com_nums = combinations(nums, 4)

result = []
for item in com_nums:
    if sum(list(item)) == 4 and item not in result and check_similar(item, result) == False:
        result.append(item)

print(result)