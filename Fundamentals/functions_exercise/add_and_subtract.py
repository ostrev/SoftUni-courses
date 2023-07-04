def sum_numbers(num_1, num_2):
    return num_1 + num_2


def subtract(sum_1, num_3):
    return sum_1 - num_3


def add_and_subtract(num_1, num_2, num_3):
    result = sum_numbers(num_1, num_2)
    return subtract(result, num_3)


first = int(input())
second = int(input())
third = int(input())

print(add_and_subtract(first, second, third))