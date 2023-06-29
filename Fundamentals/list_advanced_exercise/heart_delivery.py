houses = [int(num) for num in input().split('@')]
command = input().split()
current_position = 0
count_failed = 0
count_success = 0
while command[0] != 'Love!':
    step = int(command[1])
    current_position += step
    if current_position >= len(houses):
        current_position = 0

    houses[current_position] -= 2
    if houses[current_position] <= -2:
        print(f"Place {current_position} already had Valentine's day.")

    elif houses[current_position] <= 0:
        print(f"Place {current_position} has Valentine's day.")
        houses[current_position] = 0

    command = input().split()

print(f"Cupid's last position was {current_position}.")
for i in houses:
    if i > 0:
        count_failed += 1
    elif i <= 0:
        count_success += 1

if len(houses) - count_success == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {count_failed} places.")
