# number = int(input())
#
# large_numb = sorted([i for i in str(number)], reverse=True)
# large_numb = int(''.join(large_numb))
# print(large_numb)
# ------------
# number = int(input())
# ще изтриеш част от стойността ако започва с нули. От "00123" ще получиш само 123.
# Няма нужда да го превръщаш в int след като сортирането е върху цифри(тоест числа между 0 и 9), а не върху числа
# --------------------

number = list(input())
number.sort(reverse=True)
print(''.join(number))