def round_list():
    result = list(map(float, numbers_round))
    result = [round(i) for i in result]
    return result


numbers_round = input().split()

print(round_list())
