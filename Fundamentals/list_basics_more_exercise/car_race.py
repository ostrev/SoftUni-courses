numbers = input().split()
numbers = list(map(int, numbers))
mid_len = len(numbers) // 2

left_car_time = 0
right_car_time = 0

left_list = numbers[0:mid_len]
right_list = numbers[len(numbers):mid_len: -1]
winner = ''
for car in left_list:
    if car == 0:
        left_car_time = left_car_time*0.8
    else:
        left_car_time += car
for car in right_list:
    if car == 0:
        right_car_time = right_car_time*0.8
    else:
        right_car_time += car
if right_car_time > left_car_time:
    winner = 'left'
    total_time = left_car_time
else:
    winner = 'right'
    total_time = right_car_time

# print(left_car_time)
# print(right_car_time)
print(f'The winner is {winner} with total time: {total_time:.1f}')
