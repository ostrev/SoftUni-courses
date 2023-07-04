def perfect_number(num):
    list_divisors = []
    for i in range(1, num//2 + 1):
        if num % i == 0:
            list_divisors.append(i)
    if sum(list_divisors) == num:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")
    return num


number = int(input())
perfect_number(number)

# divisors = [1]
# a = int(input())
# c = a // 2+1
# for i in range(2, c):
#     if a % i == 0:
#         divisors.append(i)
# if sum(divisors) == a:
#     print("We have a perfect number!")
# else:
#     print("It's not so perfect.")