def min_max_sum(num):
    result = list(map(int, num))
    min_list = min(result)
    max_list = max(result)
    sum_list = sum(result)
    return [min_list, max_list, sum_list]


number = input().split()
func_result = min_max_sum(number)


print(f"The minimum number is {min_max_sum(number)[0]}")
print(f"The maximum number is {func_result[1]}")
print(f"The sum number is: {func_result[2]}")
