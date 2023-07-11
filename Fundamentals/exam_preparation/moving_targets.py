targets = [int(s) for s in input().split()]
command = input()
result = []
while command != 'End':
    data = command.split()
    if data[0] == 'Shoot':
        index = int(data[1])
        power = int(data[2])
        if 0 <= index < len(targets):
            targets[index] -= power
            if targets[index] <= 0:
                targets.pop(index)

    elif data[0] == 'Add':
        index = int(data[1])
        value = int(data[2])
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif data[0] == 'Strike':
        index = int(data[1])
        radius = int(data[2])
        if 0 <= index < len(targets)\
            and 0 <= (index - radius) < len(targets) \
            and 0 <= (index + radius) < len(targets):
            result = targets[:(index - radius):] + targets[(index + radius + 1)::]
            targets = result
        else:
            print("Strike missed!")

    command = input()

print('|'.join([str(s) for s in targets]))
