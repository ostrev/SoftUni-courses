number_of_wagon = int(input())
wagon = [0] * number_of_wagon
command = input()
while not command == 'End':
    command = command.split()
    if command[0] == 'add':
        wagon[number_of_wagon - 1] += int(command[1])
    elif command[0] == 'insert':
        wagon[int(command[1])] += int(command[2])
    else:
        wagon[int(command[1])] -= int(command[2])
    command = input()
print(wagon)
