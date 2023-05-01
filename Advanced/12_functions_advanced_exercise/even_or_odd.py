def even_odd(*args):
    result = []
    command = args[-1]
    numbers = args[:-1]
    if command == 'even':
        for num in numbers:
            if num % 2 == 0:
                result.append(num)
    else:
        for num in numbers:
            if num % 2 != 0:
                result.append(num)
    return result


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
