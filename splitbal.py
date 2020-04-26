# Get max splitted balanced strings

s = "RLRRRLLRLL"

result = 0
stack = []

for ind, ch in enumerate(list(s)):
    print(ch)

    if len(stack) is 0:
        result += 1
        stack.append(ch)
        print(stack)

    else:
        if stack[-1] == ch:
            stack.append(ch)
            print(stack)
        else:
            stack.pop()
            print(stack)



print(result)






