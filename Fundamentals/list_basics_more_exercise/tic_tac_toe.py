first_line = input().split()
second_line = input().split()
third_line = input().split()
winner_0 = False
winner_1 = False
winner_2 = False


# rows check
if first_line[0] == second_line[0] == third_line[0]:
    if first_line[0] == '1':
        winner_1 = True
    elif first_line[0] == '2':
        winner_2 = True
    else:
        winner_0 = True
if first_line[1] == second_line[1] == third_line[1]:
    if first_line[1] == '1':
        winner_1 = True
    elif first_line[1] == '2':
        winner_2 = True
    else:
        winner_0 = True
if first_line[2] == second_line[2] == third_line[2]:
    if first_line[2] == '1':
        winner_1 = True
    elif first_line[2] == '2':
        winner_2 = True
    else:
        winner_0 = True


# lines check
if first_line[0] == first_line[1] == first_line[2]:
    if first_line[0] == '1':
        winner_1 = True
    elif first_line[0] == '2':
        winner_2 = True
    else:
        winner_0 = True
if second_line[0] == second_line[1] == second_line[2]:
    if second_line[0] == '1':
        winner_1 = True
    elif second_line[0] == '2':
        winner_2 = True
    else:
        winner_0 = True
if third_line[0] == third_line[1] == third_line[2]:
    if third_line[0] == '1':
        winner_1 = True
    elif third_line[0] == '2':
        winner_2 = True
    else:
        winner_0 = True

# diagonals check

if first_line[0] == second_line[1] == third_line[2]:
    if first_line[0] == '1':
        winner_1 = True
    elif first_line[0] == '2':
        winner_2 = True
    else:
        winner_0 = True
if first_line[2] == second_line[1] == third_line[0]:
    if first_line[2] == '1':
        winner_1 = True
    elif first_line[2] == '2':
        winner_2 = True
    else:
        winner_0 = True

if winner_1:
    print('First player won')
elif winner_2:
    print('Second player won')
else:
    print('Draw!')