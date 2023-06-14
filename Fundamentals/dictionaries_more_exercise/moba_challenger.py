command = input()
players_pool = {}
total_skill = {}
is_break =False
while command != 'Season end':
    if ' -> ' in command:
        player, position, skill = command.split(' -> ')
        skill = int(skill)
        if player not in players_pool:
            players_pool[player] = {}
            if position not in players_pool[player]:
                players_pool[player][position] = skill
            else:
                if skill > players_pool[player][position]:
                    players_pool[player][position] = skill
        else:
            if position not in players_pool[player]:
                players_pool[player][position] = skill
            else:
                if skill > players_pool[player][position]:
                    players_pool[player][position] = skill
    elif' vs ' in command:
        first_pl, second_pl = command.split(' vs ')
        if first_pl in players_pool and second_pl in players_pool:

            for k in players_pool[first_pl]:
                for kk in players_pool[second_pl]:
                    if k == kk:

                        total_one = sum(players_pool[first_pl].values())
                        total_two = sum(players_pool[second_pl].values())
                        if total_one > total_two:
                            del players_pool[second_pl]
                            is_break = True
                            break
                        elif total_one < total_two:
                            del players_pool[first_pl]
                            is_break = True
                            break
                if is_break:
                    break
    command = input()

for k, v in players_pool.items():
    for kk, vv in v.items():
        total_skill[k] = sum(players_pool[k].values())
total_skill_sor = dict(sorted(total_skill.items(), key=lambda kvpt: (-kvpt[1], kvpt[0])))
for player, tot_sk in total_skill_sor.items():
    print(f'{player}: {tot_sk} skill')
    for k, v in sorted(players_pool[player].items(), key=lambda kvp: (-kvp[1], kvp[0])):
        print(f'- {k} <::> {v}')


