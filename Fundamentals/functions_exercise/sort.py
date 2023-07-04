def sort_num(num):
    result = []
    result = list(map(int, num))
    result = list(sorted(result))
    return result


number = input().split()
print(sort_num(number))
