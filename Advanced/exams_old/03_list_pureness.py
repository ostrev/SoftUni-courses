# def best_list_pureness(lst, count):
#     from collections import deque as dq
#     lst = dq(lst)
#     best = float('-inf')
#     best_rotation = 0
#     for rotation in range(count + 1):
#         result = 0
#         for i, v in enumerate(lst):
#             result += i * v
#         if result > best:
#             best = result
#             best_rotation = rotation
#         lst.appendleft(lst.pop())
#     return f'Best pureness {best} after {best_rotation} rotations'
#
#
#
# test = ([4, 3, 2, 6], 4)
# result = best_list_pureness(*test)
# print(result)
#
# test = ([7, 9, 2, 5, 3, 4], 3)
# result = best_list_pureness(*test)
# print(result)
#
# test = ([1, 2, 3, 4, 5], 10)
# result = best_list_pureness(*test)
# print(result)

def best_list_pureness(data, rotation):
    from collections import deque
    order = deque(data)
    max_result = 0
    for index in range(rotation + 1):
        current_sum = 0
        for x, y in enumerate(order):
            current_sum += x*y
        if current_sum > max_result:
            max_result = current_sum
            count_rotations = index
        order.rotate(1)
    return f'Best pureness {max_result} after {count_rotations} rotations'


