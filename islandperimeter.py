grid = [[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]


count = 0
for indi, i in enumerate(grid):
    for indj, j in enumerate(i):
        if j == 1:
            count += 4
        if indi-1>=0:
            if grid[indi-1][indj]==1:
                count-=1
        if indj-1>=0:
            if grid[indi][indj-1]==1:
                count-=1
        if indi+1 <= len(grid)-1:
            if grid[indi+1][indj]==1:
                count-=1
        if indj+1<=len(i)-1:
            if grid[indi][indj+1]==1:
                count-=1
print(count)

