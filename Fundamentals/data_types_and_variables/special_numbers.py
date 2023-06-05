n = int(input())
special = False

for num in range(1, n+1):
    first_dig = int(num / 10)
    # print(first_dig)

    second_dig = num % 10
    # print(second_dig)

    sum_dig = first_dig + second_dig
    # print(sum_dig)

    if sum_dig == 5 or sum_dig == 7 or sum_dig == 11:
        special = True
    print(f'{num} -> {special}')
    special = False
