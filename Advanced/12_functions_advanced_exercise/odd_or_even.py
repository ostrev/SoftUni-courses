def odd_fun(numbers):
    for num in numbers:
        if num % 2 != 0:
            odd_list.append(num)
    return sum(odd_list) * len(line)


def even_fun(numbers):
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)
    return sum(even_list) * len(line)


command = input()

line = [int(s) for s in input().split()]
odd_list = []
even_list = []
if command == 'Odd':
    print(odd_fun(line))
if command == 'Even':
    print(even_fun(line))
