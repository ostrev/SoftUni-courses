import sys

max_number = - sys.maxsize

for i in range(0, 3):
    number = int(input())
    if max_number < number:
        max_number = number
print(max_number)