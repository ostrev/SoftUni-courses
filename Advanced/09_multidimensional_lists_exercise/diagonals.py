size = int(input())

matrix = []
primary_diagonal = []
secondary_diagonal = []

for _ in range(size):
    line = [int(s) for s in input().split(", ")]
    matrix.append(line)

for i in range(size):
    primary_diagonal.append(matrix[i][i])
prim_d = [str(s) for s in primary_diagonal].copy()

print(f'Primary diagonal: {", ".join(prim_d)}. Sum: {sum(primary_diagonal)}')

for i in range(size):
    secondary_diagonal.append(matrix[i][size - 1 - i])

print(f'Secondary diagonal: {", ".join([str(s) for s in secondary_diagonal].copy())}. Sum: {sum(secondary_diagonal)}')
