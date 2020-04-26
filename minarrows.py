points = [[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]

ret, shoot = 0, float('inf')
for s, e in sorted(points, reverse=True):
    if shoot > e:
        shoot = s
        ret += 1

print(ret)
