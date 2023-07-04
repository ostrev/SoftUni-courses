def sum_odd_even(num):
    result = []
    for i in num:
        result.append(i)
    result_int = list(map(int, result))
    result_int_odd = sum([i for i in result_int if i % 2])
    result_int_even = sum([i for i in result_int if i % 2 == 0])
    return result_int_odd, result_int_even


number = input()
tuple_result = (sum_odd_even(number))

print(f'Odd sum = {tuple_result[0]}, Even sum = {tuple_result[1]}')





# print(result)
# print(result_int)
# print(result_int_odd)
# print(result_int_even)