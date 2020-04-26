x = 1
y = 4

bin_x = '{0:08b}'.format(x)
bin_y = '{0:08b}'.format(y)


print(bin_x)
print(bin_y)

count_mismatch = 0

bin_x_list = list(bin_x)
bin_y_list = list(bin_y)

if len(bin_x_list) > len(bin_y_list):
    for i in range(len(bin_x_list) - len(bin_y_list)):
        bin_y_list.insert(0, '0')

elif len(bin_x_list) < len(bin_y_list):
    for i in range(len(bin_y_list) - len(bin_x_list)):
        bin_x_list.insert(0, '0')

for i,v in enumerate(bin_y_list):
    if v != bin_x_list[i]:
        count_mismatch += 1


print(count_mismatch)