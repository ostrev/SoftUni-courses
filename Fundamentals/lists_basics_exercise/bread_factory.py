events = input().split('|')
energy = 100
coins = 100
gained_energy = 0
is_open = True
for event in events:
    if 'rest' in event:
        event = event.split('-')
        if int(event[1]) + energy < 100:
            gained_energy = int(event[1])
            energy += int(event[1])
        print(f'You gained {gained_energy} energy.')
        print(f'Current energy: {energy}.')

    elif 'order' in event:
        event = event.split('-')
        if energy >= 30:
            coins += int(event[1])
            energy -= 30
            print(f'You earned {int(event[1])} coins.')
        else:
            energy += 50
            print('You had to rest!')
    else:
        event = event.split('-')
        if coins > int(event[1]):
            coins -= int(event[1])
            print(f'You bought {event[0]}.')
        else:
            print(f'Closed! Cannot afford {event[0]}.')
            is_open = False
            break
if is_open:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
