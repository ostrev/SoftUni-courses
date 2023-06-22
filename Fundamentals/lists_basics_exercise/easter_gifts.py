gifts = input().split()

command = input()

while command != "No Money":
    command = command.split()
    if command[0] == 'OutOfStock':
        i = 0
        while i < len(gifts):
            if command[1] in gifts[i]:
                gifts.remove(gifts[i])
                gifts.insert(i, 'None')
            i += 1
        # gifts = ['None' if x == command[1] else x for x in gifts]
        # print(gifts)
    elif command[0] == 'Required':
        if 0 < int(command[2]) < (len(gifts) - 1):
            gifts.remove(gifts[int(command[2])])
            gifts.insert(int(command[2]), command[1])
            # gifts = [command[1] for x in gifts]
            # print(gifts)
    elif command[0] == 'JustInCase':
        gifts.remove(gifts[-1])
        gifts.append(command[1])
    command = input()

while 'None' in gifts:
    gifts.remove('None')

print(' '.join(gifts))
