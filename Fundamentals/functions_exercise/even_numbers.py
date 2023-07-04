def even_number(num):
    result = []
    result = list(map(int, num))
    # result = list(filter(lambda x: x % 2 != 0, result))
    result = list(filter(lambda x: x % 2 == 0, result))
    return result


number = input().split()
print(even_number(number))
