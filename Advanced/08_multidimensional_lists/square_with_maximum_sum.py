import sys

rows, cols = [int(s) for s in input().split(', ')]
matrix = []

for _ in range(rows):
    matrix.append([int(s) for s in input().split(', ')])

result_matrix = []
temp_matrix = []
max_sum = -sys.maxsize
current_sum = 0
for i in range(rows-1):
    for j in range(cols-1):
        temp_matrix = [matrix[i][j], matrix[i][j + 1], matrix[i+1][j], matrix[i+1][j+1]]
        current_sum = sum(temp_matrix)

        if current_sum > max_sum:
            max_sum = current_sum
            result_matrix = temp_matrix.copy()
print(result_matrix[0], result_matrix[1])
print(result_matrix[2], result_matrix[3])
print(max_sum)
