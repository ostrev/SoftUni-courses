def factorial_div(num_1, num_2):
    pass
    fact_one = 1
    fact_two = 1
    for i in range(1, num_1 + 1):
        fact_one *= i
    for i in range(1, num_2 + 1):
        fact_two *= i
    result = fact_one / fact_two
    return result


number_one = int(input())
number_two = int(input())
print(f'{factorial_div(number_one, number_two):.2f}')
