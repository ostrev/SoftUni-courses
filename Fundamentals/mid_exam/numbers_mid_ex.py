numbers_list = [int(s) for s in input().split()]

command = input().split()
while command[0] != 'Finish':

    if command[0] == 'Add':
        value = int(command[1])
        numbers_list.append(value)

    elif command[0] == 'Remove':
        value = int(command[1])
        if value in numbers_list:
            numbers_list.remove(value)

    elif command[0] == 'Replace':
        value = int(command[1])
        replacement = int(command[2])
        if value in numbers_list:
            index = numbers_list.index(value)
            numbers_list[index] = replacement

    elif command[0] == 'Collapse':
        value = int(command[1])
        numbers_list = [s for s in numbers_list if s >= value]

    command = input().split()

result = [str(numbers) for numbers in numbers_list]
print(' '.join([str(numbers) for numbers in numbers_list]))
