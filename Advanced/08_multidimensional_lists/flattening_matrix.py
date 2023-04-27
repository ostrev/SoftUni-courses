rows = int(input())
matrix = []
for _ in range(rows):
    line = [int(x) for x in input().split(', ')]
    matrix.extend(line)

print(matrix)

