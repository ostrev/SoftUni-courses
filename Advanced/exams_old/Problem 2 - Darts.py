from math import ceil


def corresponding_nums(ma, row, col):
    score = 0
    for i in range(7):
        if ma[i][col].isdigit():
            score += int(ma[i][col])

    for j in range(7):
        if ma[row][j].isdigit():
            score += int(ma[row][j])
    return score


first_player, second_player = input().split(', ')

players = {
    first_player: 501,
    second_player: 501
}

matrix = [input(). split() for _ in range(7)]
count_player = 0
active_player = ''
while True:
    if count_player % 2 == 0:
        active_player = first_player
    else:
        active_player = second_player

    count_player += 1

    row, col = [int(s) for s in eval(input())]
    try:
        hit = matrix[row][col]
        if hit.isdigit():
            players[active_player] -= int(hit)
        elif hit == 'D':
            hit = 2 * corresponding_nums(matrix, row, col)
            players[active_player] -= int(hit)
        elif hit == 'T':
            hit = 3 * corresponding_nums(matrix, row, col)
            players[active_player] -= int(hit)
        elif hit == 'B':
            break

    except IndexError:
        continue

    if players[active_player] <= 0:
        break

print(f'{active_player} won the game with {ceil(count_player / 2)} throws!')

