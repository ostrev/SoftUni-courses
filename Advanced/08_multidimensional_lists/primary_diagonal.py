size = int(input())
matrix = []
for _ in range(size):
    line = [int(s) for s in input().split()]
    matrix.append(line)
# print(matrix)
sum_mat = 0
for row_index in range(size):
    sum_mat += matrix[row_index][row_index]
print(sum_mat)