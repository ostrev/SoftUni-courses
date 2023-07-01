import math


def close_to_center(a, b, c, d):
    l1 = math.sqrt(a**2 + b**2)
    l2 = math.sqrt(c**2 + d**2)
    if l1 <= l2:
        return f'({math.floor(a)}, {math.floor(b)})'
    else:
        return f'({math.floor(c)}, {math.floor(d)})'


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print(close_to_center(x1, y1, x2, y2))