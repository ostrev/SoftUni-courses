rows, cols = [int(s) for s in input().split()]
matrix = []

for i in range(rows):
    line = []
    for j in range(cols):
        char = chr(97 + i)
        mid_char = chr(97 + i + j)
        element = char + mid_char + char
        line.append(element)
    print(*line, sep=' ')
