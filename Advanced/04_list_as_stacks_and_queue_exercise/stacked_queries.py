number = int(input())
stack = []
for _ in range(number):
    line = input().split()
    type_n = int(line[0])
    if type_n == 1:
        stack.append(int(line[1]))
    elif type_n == 2:
        if stack:
            stack.pop()
    elif type_n == 3:
        if stack:
            print(max(stack))
    elif type_n == 4:
        if stack:
            print(min(stack))

while stack:
    if len(stack) == 1:
        print(stack.pop(), end='')
    else:
        print(stack.pop(), end=', ')

# stack = [str(s) for s in stack]
# print(' '.join(stack))
