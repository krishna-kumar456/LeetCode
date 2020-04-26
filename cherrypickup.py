grid = [[0, 1, -1],
 [1, 0, -1],
 [1, 1,  1]]

# Start to end - right or down
# End to Start - left or up

cherry_count = 0

i = 0
j = 0

while i < 3:
    while j < 3:
        if grid[i][j] == -1:
            if grid[i+1][j] == -1:
                break
            else:
                continue

        elif grid[i][j] == 1:
            cherry_count += 1
            j = j + 1

        else:
            j = j + 1
    i = i + 1


while i > -1:
    while j > -1:
        if grid[i][j] == -1:
            if grid[i-1][j] == -1:
                break

        elif grid[i][j] == 1:
            cherry_count += 1

        else:
            j = j - 1
    i = i - 1

print(cherry_count)