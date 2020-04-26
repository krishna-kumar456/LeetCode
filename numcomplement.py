num =  1

temp = bin(num)

print(temp)


rev_temp = ""

for item in temp[2:]:
    if item == '1':
        rev_temp += '0'
    else:
        rev_temp += '1'

print(int(rev_temp, 2))