n = int(input())
sum_chars = 0
for i in range(1, n+1):
    char = input()
    sum_chars += ord(char)

print(f'The sum equals: {sum_chars}')