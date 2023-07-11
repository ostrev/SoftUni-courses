def swap_position(numbers_list, index_1, index_2):
    numbers_list[index_1], numbers_list[index_2] = numbers_list[index_2], numbers_list[index_1]
    return numbers_list


def multiply_position(numbers_list, index_1, index_2):
    numbers_list[index_1] = numbers_list[index_1] * numbers_list[index_2]
    return numbers_list


array = [int(num) for num in input().split()]
commands = input()

while commands != 'end':
    command = commands.split()
    word = command[0]
    if word == 'swap':
        index_one = int(command[1])
        index_two = int(command[2])
        swap_position(array, index_one, index_two)
    elif word == 'multiply':
        index_one = int(command[1])
        index_two = int(command[2])
        multiply_position(array, index_one, index_two)
    elif word == 'decrease':
        array = [s - 1 for s in array]

    commands = input()

print(', '.join([str(n) for n in array]))
