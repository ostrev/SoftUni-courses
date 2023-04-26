from collections import deque
from datetime import datetime, timedelta

input_line = input().split(';')
robots = []
robot_info = []

start_time = datetime.strptime(input(), '%H:%M:%S')
for robot in input_line:
    robot_info = robot.split('-')
    processing_time = int(robot_info[1])
    robot_info.append(start_time)
    robots.append(robot_info)

queue = deque()
command = input()
while command != 'End':
    queue.append(command)
    command = input()

while queue:
    item = queue.popleft()
    start_time = start_time + timedelta(seconds=1)

    for rob in robots:
        if start_time >= rob[2]:
            print(f"{rob[0]} - {item} [{start_time.strftime('%H:%M:%S')}]")
            rob[2] = start_time + timedelta(seconds=int(rob[1]))
            break
    else:
        queue.append(item)


# ****************************************
from math import floor
from collections import deque


class Robot:
    def __init__(self, name, processing_time):
        self.name = name
        self.processing_time = processing_time
        self.busy_until = 0


def get_seconds_from_time(time):
    hours, minutes, seconds = [int(x) for x in time.split(':')]
    return hours * 60 * 60 + minutes * 60 + seconds


def get_time_from_seconds(seconds):
    # 90 000
    # 100 000
    seconds %= (24 * 60 * 60)
    hours = seconds // (60 * 60)
    minutes = floor((seconds / 60) % 60)
    seconds = seconds % 60
    return f'{hours:02d}:{minutes:02d}:{seconds:02d}'


robots = []
robots_input = input().split(';')
for robot_input in robots_input:
    robot_name, processing_time = robot_input.split('-')
    robots.append(Robot(robot_name, int(processing_time)))

time_in_seconds = get_seconds_from_time(input())
items = deque()

while True:
    item = input()
    if item == 'End':
        break
    items.append(item)

while items:
    current_item = items.popleft()
    time_in_seconds += 1
    found_robot = False
    for robot in robots:
        if time_in_seconds >= robot.busy_until:
            robot.busy_until = time_in_seconds + robot.processing_time
            found_robot = True
            print(f'{robot.name} - {current_item} [{get_time_from_seconds(time_in_seconds)}]')
            break
    if not found_robot:
        items.append(current_item)