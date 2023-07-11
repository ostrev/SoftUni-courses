initial_loot = input().split('|')
command = input().split()
steal_list = []
gain_sum = 0
while command[0] != 'Yohoho!':
    if command[0] == 'Loot':
        for item in command[1::]:
            if item not in initial_loot:
                initial_loot.insert(0, item)

    elif command[0] == 'Drop':
        if 0 <= int(command[1]) < len(initial_loot):
            drop = initial_loot.pop(int(command[1]))
            initial_loot.append(drop)

    elif command[0] == 'Steal':
        steal_list = []
        if int(command[1]) >= len(initial_loot):
            abs_value = len(initial_loot)
        else:
            abs_value = int(command[1])
        for _ in range(abs_value):
            steal = initial_loot.pop(-1)
            steal_list.insert(0, steal)
        print(', '.join(steal_list))
    command = input().split()
if len(initial_loot) == 0:
    print("Failed treasure hunt.")
else:
    for item in initial_loot:
        gain_sum += len(item)
    average = gain_sum / len(initial_loot)
    print(f"Average treasure gain: {average:.2f} pirate credits.")
