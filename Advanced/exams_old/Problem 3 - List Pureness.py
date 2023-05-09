from collections import deque


def best_list_pureness(*args):
    list_rev = deque(args[0])
    num = args[1] + 1
    max = 0
    res_sum = 0
    res_rot = 0
    max_dic = {}
    while num != 0:
        num -= 1
        res_rot += 1
        for i in range(len(list_rev)):
            res_sum += list_rev[i]*i
        max_dic[res_rot - 1] = res_sum
        if res_sum > max:
            max = res_sum
        res_sum = 0
        temp = list_rev.pop()
        list_rev.appendleft(temp)

    max_dict = sorted(max_dic.items(), key=lambda kvpt: -kvpt[1])
    max_rot = 0
    for k, v in max_dict:
        max_rot = k
        break
    return f'Best pureness {max} after {max_rot} rotations'


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
