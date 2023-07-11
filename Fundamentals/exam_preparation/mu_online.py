health = 100
bitcoins = 0

rooms = input().split('|')
room_count = 0
for element in rooms:
    room = element.split()
    command = room[0]
    number = int(room[1])
    room_count += 1
    if command == 'potion':
        if (health + number) > 100:
            number = 100 - health
        health += number
        print(f"You healed for {number} hp.")
        print(f"Current health: {health} hp.")
    elif command == 'chest':
        bitcoins += number
        print(f"You found {number} bitcoins.")
    else:
        health -= number
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {room_count}")
            exit()
print(f"You've made it!")
print(f"Bitcoins: {bitcoins}")
print(f"Health: {health}")



