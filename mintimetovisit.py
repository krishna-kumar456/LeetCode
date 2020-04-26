points = [[1,1],[3,4],[-1,0]]

min_time = 0

for i, v in enumerate(points):
    current_pos = v
    next_dest = []

    if i + 1 < len(points):
        next_dest = points[i+1]
    else:
        break

    while current_pos != next_dest:
        if (current_pos[0] < next_dest[0] and current_pos[1] < next_dest[1]):
            current_pos[0] += 1
            current_pos[1] += 1
            min_time += 1

        elif (current_pos[0] > next_dest[0] and current_pos[1] > next_dest[1]):
            current_pos[0] -= 1
            current_pos[1] -= 1
            min_time += 1

        elif current_pos[0] > next_dest[0] and current_pos[1] == next_dest[1]:
            current_pos[0] -= 1
            min_time += 1

        elif current_pos[0] < next_dest[0] and current_pos[1] == next_dest[1]:
            current_pos[0] += 1
            min_time += 1

        elif current_pos[0] == next_dest[0] and current_pos[1] < next_dest[1]:
            current_pos[1] += 1
            min_time += 1

        elif current_pos[0] == next_dest[0] and current_pos[1] > next_dest[1]:
            current_pos[1] -= 1
            min_time += 1


print(min_time)




