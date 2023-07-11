def is_index_valid(index, length):
    if 0 <= index < length:
        return True


pirate_ship = [int(num) for num in input().split('>')]
war_ship = [int(num) for num in input().split('>')]
health_capacity = int(input())
command = input().split()

while command[0] != 'Retire':
    word = command[0]
    if word == 'Fire':
        index_fire = int(command[1])
        damage_fire = int(command[2])
        if is_index_valid(index_fire, len(war_ship)):
            war_ship[index_fire] -= damage_fire
            if war_ship[index_fire] <= 0:
                print("You won! The enemy ship has sunken.")
                exit()
    elif word == 'Defend':
        start_index = int(command[1])
        end_index = int(command[2])
        damage_defend = int(command[3])
        if is_index_valid(start_index, len(pirate_ship)) and is_index_valid(end_index, len(pirate_ship)):
            for i in range(start_index, end_index + 1):
                pirate_ship[i] -= damage_defend
                if pirate_ship[i] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    exit()
    elif word == 'Repair':
        index_repair = int(command[1])
        health = int(command[2])
        if is_index_valid(index_repair, len(pirate_ship)):
            pirate_ship[index_repair] += health
            if pirate_ship[index_repair] > health_capacity:
                pirate_ship[index_repair] = health_capacity

    elif word == 'Status':
        lower_section = health_capacity * 0.2
        count_status = 0
        for health_status in pirate_ship:
            if health_status < lower_section:
                count_status += 1
        print(f"{count_status} sections need repair.")
    command = input().split()
print(f"Pirate ship status: {sum(pirate_ship)}\n"
      f"Warship status: {sum(war_ship)}")
