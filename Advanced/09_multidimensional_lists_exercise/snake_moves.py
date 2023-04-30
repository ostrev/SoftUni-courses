rows, cols = [int(s) for s in input().split()]

matrix = []
index = 0
line = input()

for i in range(rows):
    row_element = []
    for j in range(cols):
        row_element.append(line[index % len(line)])
        index += 1
    if i % 2 == 0:
        matrix.append(row_element)
    else:
        row_element.reverse()
        matrix.append(row_element)

for r in matrix:
    print(*r, sep="")
