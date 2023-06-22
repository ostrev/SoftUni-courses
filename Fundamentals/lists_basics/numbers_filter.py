number = int(input())


integer_list = []

for _ in range(number):
    integers = int(input())
    integer_list.append(integers)
command = input()
if command == 'even':
    for index in range(len(integer_list)-1, -1, -1):
        el = integer_list[index]
        if el % 2 != 0:
            integer_list.remove(el)
elif command == 'odd':
    for index in range(len(integer_list)-1, -1, -1):
        el = integer_list[index]
        if el % 2 == 0:
            integer_list.remove(el)
elif command == 'negative':
    for index in range(len(integer_list)-1, -1, -1):
        el = integer_list[index]
        if el >= 0:
            integer_list.remove(el)
elif command == 'positive':
    for index in range(len(integer_list)-1, -1, -1):
        el = integer_list[index]
        if el < 0:
            integer_list.remove(el)
print(integer_list)