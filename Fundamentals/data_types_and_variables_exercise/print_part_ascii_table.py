first_n = int(input())
second_n = int(input())

for i in range(first_n, second_n + 1):
    chars = chr(i)
    print(f'{chars} ', end='')

