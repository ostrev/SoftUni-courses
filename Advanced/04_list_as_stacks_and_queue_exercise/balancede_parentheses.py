from collections import deque

line = list(input())
if len(line) % 2 != 0:
    print('NO')
    exit()
queue = deque(line)
stack = []
i = 0
is_true = 0
while queue:
    if line[i] == '{' or line[i] == '[' or line[i] == '(':
        stack.append(queue.popleft())
        i += 1
    else:
        if queue[0] == ')':
            if stack.pop() == '(':
                is_true += 1
                queue.popleft()
            else:
                break
        elif queue[0] == ']':
            if stack.pop() == '[':
                is_true += 1
                queue.popleft()
            else:
                break
        elif queue[0] == '}':
            if stack.pop() == '{':
                is_true += 1
                queue.popleft()
            else:
                break
        i += 1
if is_true == len(line)/2:
    print('YES')
else:
    print('NO')

# *****************
from collections import deque
parenthesis = list(input())
parenthesis = deque(parenthesis)
queue = deque()
stack = []
is_balanced = True
if len(parenthesis) % 2 != 0:
    print('NO')
    exit()
while parenthesis:
    char = parenthesis.popleft()
    if char == '[':
        stack.append(char)
    elif char == '{':
        stack.append(char)
    elif char == '(':
        stack.append(char)
    elif char == ']':
        if stack.pop() != '[':
            is_balanced = False
            print('NO')
            break
    elif char == '}':
        if stack.pop() != '{':
            is_balanced = False
            print('NO')
            break
    elif char == ')':
        if stack.pop() != '(':
            is_balanced = False
            print('NO')
            break

if is_balanced:
    if len(stack) != len(parenthesis):
        print('NO')
    else:
        print('YES')
