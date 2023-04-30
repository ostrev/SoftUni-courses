line = input().split('|')
result = []
while line:
    sub_line = line.pop().split()
    for el in sub_line:
        result.append(el)

print(*result, sep=' ')
