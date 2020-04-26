first_nine_letters = list(map(chr, range(97, 106)))
mapping = {str(i):first_nine_letters[i-1] for i in range(1,10)}
other_letters = list(map(chr, range(106, 123)))
for i in range(10,27):
    mapping[str(i)+'#']=other_letters[i-10]

mapping['0'] = '0'
print(mapping)

s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
tracker = []
result = []

for i,v in enumerate(s):
    print(v)

    if v != '#':
        tracker.append(v)
        result.append(mapping[v])

    elif v == '#':
        temp = ''.join(tracker[-2:])
        result.pop()
        result.pop()
        result.append(mapping[temp + '#'])
        tracker.append(v)

print(''.join(result))


abcdefghijklmnopqrstuvwxyz
abcdefghijklmnopqrstuvwxyz




