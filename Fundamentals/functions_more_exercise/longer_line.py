import math


def length_of_line(a, b, c, d):
    dist = math.sqrt((c - a) ** 2 + (b - d) ** 2)
    return dist


def distance_to_center(a, b):
    lent = math.sqrt(a ** 2 + b ** 2)
    return lent


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

if length_of_line(x1, y1, x2, y2) >= length_of_line(x3, y3, x4, y4):
    if distance_to_center(x1, y1) <= distance_to_center(x2, y2):
        print(f'({math.floor(x1)}, {math.floor(y1)})({math.floor(x2)}, {math.floor(y2)})')
    else:
        print(f'({math.floor(x2)}, {math.floor(y2)})({math.floor(x1)}, {math.floor(y1)})')
else:
    if distance_to_center(x3, y3) <= distance_to_center(x4, y4):
        print(f'({math.floor(x3)}, {math.floor(y3)})({math.floor(x4)}, {math.floor(y4)})')
    else:
        print(f'({math.floor(x4)}, {math.floor(y4)})({math.floor(x3)}, {math.floor(y3)})')
