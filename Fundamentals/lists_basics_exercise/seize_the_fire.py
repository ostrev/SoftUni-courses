command = input().split('#')
water = int(input())
effort = 0
total_fire = 0
i = 0
print('Cells:')
while i < len(command):

    if 'High' in command[i]:
        high_command = command[i].split(' = ')
        if 81 <= int(high_command[1]) <= 125 and water >= int(high_command[1]):
            total_fire += int(high_command[1])
            water -= int(high_command[1])
            print(f' - {int(high_command[1])}')
    if 'Medium' in command[i]:
        high_command = command[i].split(' = ')
        if 51 <= int(high_command[1]) <= 80 and water >= int(high_command[1]):
            total_fire += int(high_command[1])
            water -= int(high_command[1])
            print(f' - {int(high_command[1])}')
    if 'Low' in command[i]:
        high_command = command[i].split(' = ')
        if 1 <= int(high_command[1]) <= 50 and water >= int(high_command[1]):
            total_fire += int(high_command[1])
            water -= int(high_command[1])
            print(f' - {int(high_command[1])}')
    i += 1

effort += (0.25 * total_fire)
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')
