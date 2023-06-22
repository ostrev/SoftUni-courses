team_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
win_game = False
cards = input().split()
for index in range(len(cards)):
    # card = cards[index].split('-')
    team, number = cards[index].split('-')
    number = int(number)

    if team == 'A' and number in team_a:
        team_a.remove(number)

        if len(team_a) < 7:
            print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
            print(f'Game was terminated')
            win_game = True
            break
    elif team == 'B' and number in team_b:
        team_b.remove(number)

        if len(team_b) < 7:
            print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
            print(f'Game was terminated')
            win_game = True
            break
if not win_game:
    print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")



team_a = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
team_b = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']

cards = input().split()
game_is_stop = False
for player_off in cards:
    if player_off in team_a:
        team_a.remove(player_off)
    elif player_off in team_b:
        team_b.remove(player_off)
    if len(team_a) < 7 or len(team_b) < 7:
        game_is_stop = True
        break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if game_is_stop:
    print(f'Game was terminated')
