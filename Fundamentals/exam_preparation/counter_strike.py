energy = int(input())
command = input()
win_counter = 0
while command != 'End of battle':
    if energy >= int(command):
        energy -= int(command)
        win_counter += 1
        if win_counter % 3 == 0:
            energy += win_counter
    else:
        print(f"Not enough energy! Game ends with {win_counter} won battles and {energy} energy")
        exit()
    command = input()
print(f"Won battles: {win_counter}. Energy left: {energy}")
