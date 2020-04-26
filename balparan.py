S = "()()"

stack = []
result = []

for item in list(S):
    if item == '(' and len(stack) == 0:
        stack.append(item)
    elif item == '(' and len(stack) > 0:
        stack.append(item)
        result.append(item)
    elif item == ')' and len(stack) > 1:
        stack.pop()
        result.append(item)
    elif item == ')' and len(stack) == 1:
        stack.pop()

print(''.join(result))

