rows, cols = [int(s) for s in input().split()]

matrix = []

for _ in range(rows):
    line = input().split()
    matrix.append(line)

# print(matrix)
count = 0
for i in range(rows-1):
    for j in range(cols - 1):
        first_element = matrix[i][j]
        second_element = matrix[i][j+1]
        third_element = matrix[i + 1][j]
        forth_element = matrix[i+1][j+1]

        if first_element == second_element == third_element == forth_element:
            count +=1

print(f'{count}')
