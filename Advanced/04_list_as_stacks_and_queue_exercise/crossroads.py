from collections import deque
time_green = int(input())
free_window = int(input())
command = input()
cars = deque()
temp_car = deque()
flag_free_win = True
is_green = True
total_cars_passed = 0
hit_car = ''
while command != 'END':
    if command != 'green':
        cars.append(command)
    else:
        flag_free_win = True
        if not cars:
            command = input()
            continue
        else:
            is_green = True
            hit_car = cars[0]
            timer = time_green
            temp_car = deque(cars.popleft())
            total_cars_passed += 1
            while temp_car:
                if timer > 0:
                    temp_car.popleft()
                    timer -= 1
                if not temp_car and timer > 0 and flag_free_win:
                    if cars and is_green:
                        hit_car = cars[0]
                        temp_car = deque(cars.popleft())
                        total_cars_passed += 1
                    else:
                        timer = time_green
                        break
                if timer == 0 and flag_free_win:
                    is_green = False
                    flag_free_win = False
                    timer = free_window
                if timer == 0 and not flag_free_win and temp_car:
                    print("A crash happened!")
                    print(f'{hit_car} was hit at {temp_car.popleft()}.')
                    exit()
    command = input()
print("Everyone is safe.")
print(f'{total_cars_passed} total cars passed the crossroads.')

'''
TEST 1
1
3
Hume
Merc
green
green
END
'''


from collections import deque
green_light = int(input())
window = int(input())
cars = deque()
cars_counter = 0
crashed = False
command = input()
while command != "END":
    if command == "green":
        if cars:
            current = cars.popleft()
            seconds_left = green_light - len(current)
            while seconds_left > 0:
                cars_counter += 1
                if cars:
                    current = cars.popleft()
                    seconds_left -= len(current)
                else:
                    break
            if seconds_left == 0:
                cars_counter += 1
            if window >= abs(seconds_left):
                if seconds_left < 0:
                    cars_counter += 1
            else:
                idx = window + seconds_left
                print("A crash happened!")
                print(f"{current} was hit at {current[idx]}.")
                crashed = True
                break
    else:
        cars.append(command)
    command = input()
if not crashed:
    print("Everyone is safe.")
    print(f"{cars_counter} total cars passed the crossroads.")


#************

from collections import deque

green_window = int(input())
free_window = int(input())

cars = deque()
passed_cars = 0
has_crashed = False

while True:
    line = input()
    if line == "END":
        break

    if line == "green":
        current_green = green_window
        while cars and current_green > 0:
            car = cars.popleft()
            if current_green >= len(car) or current_green + free_window >= len(car):
                passed_cars += 1
                current_green -= len(car)
            else:
                print('A crash happened!')
                print(f'{car} was hit at {car[current_green + free_window]}.')
                has_crashed = True
                break
    else:
        cars.append(line)

    if has_crashed:
        break

if not has_crashed:
    print('Everyone is safe.')