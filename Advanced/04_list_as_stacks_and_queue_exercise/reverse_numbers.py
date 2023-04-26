line = input().split()
while len(line) > 0:

    print(line.pop(), end= ' ')

# **************


numbers = input().split(' ')
stack = []
while numbers:
    stack.append(numbers.pop())
print(' '.join(stack))

