n = 15

result = []
for item in range(1, n+1):
    if item == 1:
        result.append("1")
    elif item % 3 == 0 and item % 5 == 0:
        result.append("FizzBuzz")
    elif item % 3 == 0:
        result.append("Fizz")
    elif item % 5 == 0:
        result.append("Buzz")
    else:
        result.append(str(item))

print(result)