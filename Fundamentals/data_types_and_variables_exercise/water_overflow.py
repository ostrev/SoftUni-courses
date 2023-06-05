n = int(input())

water_in_tank = 0

for i in range(n, 0, -1):
    water = int(input())
    free_water = 255 - water_in_tank

    if water <= free_water:
        water_in_tank += water
    else:
        print(f'Insufficient capacity!')
print(water_in_tank)
