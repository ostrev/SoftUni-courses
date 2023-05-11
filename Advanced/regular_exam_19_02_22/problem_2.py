def move_w(i, j, mat):
    if j == 7:
        if i - 1 > 0 and mat[i - 1][j - 1] != 'b':
            return True
        else:
            return False
    elif j == 0:
        if i - 1 > 0 and mat[i - 1][j + 1] != 'b':
            return True
        else:
            return False
    else:
        if i - 1 > 0 and mat[i - 1][j - 1] != 'b' and mat[i - 1][j + 1] != 'b':
            return True
        else:
            return False


def move_b(i, j, mat):
    if j == 7:
        if i + 1 < 7 and mat[i + 1][j - 1] != 'w':
            return True
        else:
            return False
    elif j == 0:
        if i + 1 < 7 and mat[i + 1][j + 1] != 'w':
            return True
        else:
            return False
    else:
        if i + 1 < 7 and mat[i + 1][j - 1] != 'w' and mat[i + 1][j + 1] != 'w':
            return True
        else:
            return False


matrix = []

w_row = 0
w_col = 0

b_row = 0
b_col = 0


for row in range(8):
    line = list(input().split())
    matrix.append(line)
    if 'w' in line:
        w_row = row
        w_col = line.index('w')
    if 'b' in line:
        b_row = row
        b_col = line.index('b')

while True:

    if move_w(w_row, w_col, matrix):
        w_row -= 1
        matrix[w_row][w_col] = 'w'
    else:
        if w_col == 7:
            if matrix[w_row - 1][w_col - 1] == 'b':
                one = w_col - 1
                one = chr(97 + one)
                two = 8 - (w_row - 1)
                print(f"Game over! White win, capture on {one}{two}.")
                break
            else:  # reach the end
                one = w_col
                one = chr(97 + one)
                two = 8 - (w_row - 1)
                print(f"Game over! White pawn is promoted to a queen at {one}{two}.")
                break
        elif w_col == 0:
            if matrix[w_row - 1][w_col + 1] == 'b':
                one = w_col + 1
                one = chr(97 + one)
                two = 8 - (w_row - 1)
                print(f"Game over! White win, capture on {one}{two}.")
                break
            else:  # reach the end
                one = w_col
                one = chr(97 + one)
                two = 8 - (w_row - 1)
                print(f"Game over! White pawn is promoted to a queen at {one}{two}.")
                break
        else:
            if matrix[w_row - 1][w_col - 1] == 'b':
                one = w_col - 1
                one = chr(97 + one)
                two = 8 - (w_row - 1)
                print(f"Game over! White win, capture on {one}{two}.")
                break

            elif matrix[w_row - 1][w_col + 1] == 'b':
                one = w_col + 1
                one = chr(97 + one)
                two = 8 - (w_row - 1)
                print(f"Game over! White win, capture on {one}{two}.")
                break
            else: # reach the end
                one = w_col
                one = chr(97 + one)
                two = 8 - (w_row - 1)
                print(f"Game over! White pawn is promoted to a queen at {one}{two}.")
                break

    if move_b(b_row, b_col, matrix):
        b_row += 1
        matrix[b_row][b_col] = 'b'
    else:
        if matrix[b_row + 1][b_col - 1] == 'w':
            one = b_col - 1
            one = chr(97 + one)
            two = 8 - (b_row + 1)
            print(f"Game over! Black win, capture on {one}{two}.")
            break
        elif matrix[b_row + 1][b_col + 1] == 'w':
            one = b_col + 1
            one = chr(97 + one)
            two = 8 - (b_row + 1)
            print(f"Game over! Black win, capture on {one}{two}.")
            break
        else: # reach the end
            one = b_col
            one = chr(97 + one)
            two = 8 - (b_row + 1)
            print(f"Game over! Black pawn is promoted to a queen at {one}{two}.")
            break



