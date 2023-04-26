from collections import deque
box_of_clothes = input().split()
box_of_clothes = [int(s) for s in box_of_clothes]
count = 1
capacity = int(input())
capacity_start = capacity
rack = 0
while box_of_clothes:
    rack = box_of_clothes.pop()
    if capacity >= rack:
        capacity -= rack
    else:
        capacity = capacity_start
        count += 1
        capacity -= rack
print(count)