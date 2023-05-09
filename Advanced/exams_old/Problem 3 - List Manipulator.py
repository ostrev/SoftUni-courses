from collections import deque as dq
def list_manipulator(list_s, command_one, command_two, *args):
    list_s = dq(list_s)
    result = []
    if command_one == 'add':
        if command_two == 'beginning':
            for num in reversed(args):
                list_s.appendleft(num)
            for i in list_s:
                result.append(i)
            return result
        elif command_two == 'end':
            for num in args:
                list_s.append(num)
            for i in list_s:
                result.append(i)
            return result
    elif command_one == 'remove':
        if command_two == 'beginning':
            if args:
                param = args[0]
                for j in range(param):
                    list_s.popleft()
            else:
                list_s.popleft()

            for i in list_s:
                result.append(i)
            return result
        elif command_two == 'end':
            if args:
                param = args[0]
                for j in range(param):
                    list_s.pop()
            else:
                list_s.pop()

            for i in list_s:
                result.append(i)
            return result



print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
# print(list_manipulator([1,2,3], "remove", "end", 2))
# print(list_manipulator([1,2,3], "remove", "beginning", 2))
