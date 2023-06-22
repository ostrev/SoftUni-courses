single_string = input().split(' ')
count = int(input())
single_string = list(map(int, single_string)) # single_string = [int(i) for i in single_string]
for i in range(1, count + 1):
    min_element = min(single_string)
    single_string.remove(min_element)

print(', '.join(map(str, single_string)))
