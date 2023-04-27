rows = int(input())
matrix = []
for _ in range(rows):
    line = [int(s) for s in input().split(', ') if int(s) % 2 == 0]
    matrix.append(line)
# event = [[x for x in row if x % 2 == 0]for row in matrix]

print(matrix)
