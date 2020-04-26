n = "PPALLL"

#attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late). 

split_n = list(n)

count_A = 0
count_L = 0

for index, item in enumerate(split_n):
    if item == 'A':
        count_A += 1
    
    if index + 1 < len(split_n):
        if item == 'L' and split_n[index + 1] == 'L':
            count_L += 1

if count_A > 1 or count_L > 2:
    print(False)
else:
    print(True)
