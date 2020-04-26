def insert_sort(arr):
    for i, v in enumerate(arr):
        print(arr)
        print(i)
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            temp = arr[j]
            arr[j] = arr[j-1]
            arr[j-1] = temp

            j = j - 1
    return arr


arr = [1, 5, 2, 10, 8]

print(insert_sort(arr))

