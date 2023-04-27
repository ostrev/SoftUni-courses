rows, cols = [int(s) for s in input().split(', ')]
matrix = []
sum_matrix = 0
for row in range(rows):
    line = [int(s) for s in input().split(', ')]
    sum_matrix += sum(line)
    matrix.append(line)
print(sum_matrix)
print(matrix)