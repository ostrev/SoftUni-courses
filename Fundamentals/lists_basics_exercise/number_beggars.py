single_strings = input().split(', ')
count_beggars = int(input())
single_strings_int = []
sum = []
sum_beggar = 0
for element in single_strings:
    element = int(element)
    single_strings_int.append(element)
for i in range(1, count_beggars + 1):
    for j in range(i-1, len(single_strings_int), count_beggars):
        el = single_strings_int[j]
        sum_beggar += el
    sum.append(sum_beggar)
    sum_beggar = 0
print(sum)
