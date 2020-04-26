n = 4

# Get reverse list of n
reverse_list = []
while n >= 1:
    reverse_list.append(n)
    n = n - 1

no_of_operations = 4

final_result = 1

for index, value in enumerate(reverse_list):
    if len(reverse_list) != index + 1:
        
        if index + 1 % no_of_operations == 1:
            if index == 0:
                final_result = value
            final_result = final_result * reverse_list[index + 1]

        elif index + 1 % no_of_operations == 2: 
            final_result = int(final_result / reverse_list[index + 1])

        elif index + 1 % no_of_operations == 3: 
            final_result = final_result + reverse_list[index + 1]

        elif index + 1 % no_of_operations == 4: 
            final_result = final_result - reverse_list[index + 1]
