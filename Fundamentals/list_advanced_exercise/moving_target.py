sequence_of_target = [int(num) for num in input().split()]
command = input().split()

while command[0] != 'End':
    action = command[0]
    index = int(command[1])
    value = int(command[2])

    if command[0] == 'Shoot':
        if 0 <= index <= len(sequence_of_target) - 1:
            sequence_of_target[index] -= value
            if sequence_of_target[index] <= 0:
                sequence_of_target.pop(index)

    elif command[0] == 'Add':
        if 0 <= index <= len(sequence_of_target) - 1:
            sequence_of_target.insert(index, value)
        else:
            print("Invalid placement!")
    elif command[0] == 'Strike':
        if index - value >= 0 and index + value <= len(sequence_of_target) - 1:
            sequence_of_target.pop(index+value)
            sequence_of_target.pop(index)
            sequence_of_target.pop(index-value)

        else:
            print("Strike missed!")

    command = input().split()
print('|'.join([str(s) for s in sequence_of_target]))
