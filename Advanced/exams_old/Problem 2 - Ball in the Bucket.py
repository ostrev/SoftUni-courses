size = 6

matrix = [input().split() for _ in range(size)]

points = 0
throw = 3
for _ in range(throw):
    row, col = [int(el) for el in eval(input())]

    try:
        if matrix[row][col] == 'B':
            matrix[row][col] = '0'
            for row_i in range(size):
                if matrix[row_i][col].isdigit():
                    points += int(matrix[row_i][col])

    except IndexError:
        continue

if points < 100:
    print(f"Sorry! You need {100 - points} points more to win a prize.")
elif 100 <= points <= 199:
    print(f"Good job! You scored {points} points, and you've won Football.")
elif 200 <= points <= 299:
    print(f"Good job! You scored {points} points, and you've won Teddy Bear.")
elif 300 <= points:
    print(f"Good job! You scored {points} points, and you've won Lego Construction Set.")



# ********************
n = 6
throws_count = 3

matrix = [input().split() for _ in range(n)]
total_points = 0

for _ in range(throws_count):
    row, col = [int(el) for el in eval(input())]

    try:
        if matrix[row][col] == "B":
            total_points += sum([int(matrix[row_index][col]) for row_index in range(n) if matrix[row_index][col].isdigit()])
            matrix[row][col] = '0'
    except IndexError:
        continue

if total_points < 100:
    print(f"Sorry! You need {100-total_points} points more to win a prize.")
elif 100 <= total_points < 200:
    print(f"Good job! You scored {total_points} points, and you've won Football.")
elif 200 <= total_points < 300:
    print(f"Good job! You scored {total_points} points, and you've won Teddy Bear.")
else:
    print(f"Good job! You scored {total_points} points, and you've won Lego Construction Set.")