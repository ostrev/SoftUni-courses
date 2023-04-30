size = int(input())

matrix = []
primary_diagonal = []
secondary_diagonal = []

for _ in range(size):
    line = [int(s) for s in input().split()]
    matrix.append(line)

for i in range(size):
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][size - 1 - i])

print(f'{abs(sum(primary_diagonal) - sum(secondary_diagonal))}')
