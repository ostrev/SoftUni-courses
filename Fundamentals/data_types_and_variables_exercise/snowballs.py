import sys

number_snowball = int(input())
max_value = -sys.maxsize
print_snowball_snow = 0
print_snowball_time = 0
print_snowball_quality = 0
for i in range(number_snowball):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = (snowball_snow / snowball_time) ** snowball_quality
    if max_value < snowball_value:
        max_value = snowball_value
        print_snowball_snow = snowball_snow
        print_snowball_time = snowball_time
        print_snowball_quality = snowball_quality
print(f'{print_snowball_snow} : {print_snowball_time} = {max_value:.0f} ({print_snowball_quality})')