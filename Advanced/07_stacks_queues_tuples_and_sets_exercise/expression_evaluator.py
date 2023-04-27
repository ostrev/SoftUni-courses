from collections import deque
line_input = deque(input().split())
temp = deque()
while line_input:
    element = line_input[0]
    if element == "+":

        if len(temp) > 1:
            first = int(temp.popleft())
            second = int(temp.popleft())
            res = first + second
            temp.appendleft(res)
        else:
            operator = line_input.popleft()
            continue
    elif element == "*":

        if len(temp) > 1:
            first = int(temp.popleft())
            second = int(temp.popleft())
            res = first * second
            temp.appendleft(res)
        else:
            operator = line_input.popleft()
            continue
    elif element == '-':

        if len(temp) > 1:
            first = int(temp.popleft())
            second = int(temp.popleft())
            res = first - second
            temp.appendleft(res)
        else:
            operator = line_input.popleft()
            continue
    elif element == "/":

        if len(temp) > 1:
            first = int(temp.popleft())
            second = int(temp.popleft())
            res = first // second
            temp.appendleft(res)
        else:
            operator = line_input.popleft()
            continue
    else:
        temp.append(line_input.popleft())

print(temp.popleft())
