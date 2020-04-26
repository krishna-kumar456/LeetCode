nums = [1,1,2,3]
result = []
freq_arr = []

for i,v in enumerate(nums):
    if i % 2 == 0 and i != len(nums) - 1:
        freq_arr.append([nums[i], nums[i+1]])

for item in freq_arr:
    for i in range(item[0]):
        result.append(item[1])

print(result)