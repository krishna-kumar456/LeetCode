intervals = [[1,4],[0,4]]

result = []

for index, item in enumerate(intervals):
    if len(intervals) == 1:
        result.append(item)
    for i2, item2 in enumerate(intervals[index+1:]):
        if item2[0] in range(item[0], item[1] + 1):
            result.append([item[0], item2[1]])
        else:
            if len(result) == 0:
                result.append(item)
            if item2 not in result:
                result.append(item2)

print(result)

