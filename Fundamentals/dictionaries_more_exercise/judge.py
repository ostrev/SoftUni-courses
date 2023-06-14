command = input()
contest_dic = {}
individual_dic = {}
total_points = {}
while command != 'no more time':
    data = command.split(' -> ')
    username = data[0]
    contest = data[1]
    points = int(data[2])
    if username not in individual_dic:
        individual_dic[username] = {}
        if contest not in individual_dic[username]:
            individual_dic[username][contest] = points
        else:
            if points > individual_dic[username][contest]:
                individual_dic[username][contest] = points
    else:
        if contest not in individual_dic[username]:
            individual_dic[username][contest] = points
        else:
            if points > individual_dic[username][contest]:
                individual_dic[username][contest] = points
    if contest not in contest_dic:
        contest_dic[contest] = {}
        if username not in contest_dic[contest]:
            contest_dic[contest][username] = points
        else:
            if points > contest_dic[contest][username]:
                contest_dic[contest][username] = points
    else:
        if username not in contest_dic[contest]:
            contest_dic[contest][username] = points
        else:
            if points > contest_dic[contest][username]:
                contest_dic[contest][username] = points
    command = input()
counter = 0
for k, v in contest_dic.items():
    print(f'{k}: {len(contest_dic[k])} participants')
    counter = 0
    for kk, vv in sorted(v.items(), key=lambda x: (-x[1], x[0])):
        counter += 1
        print(f'{counter}. {kk} <::> {vv}')
for user in individual_dic:
    sum_value = individual_dic[user].values()
    total = sum(sum_value)
    total_points[user] = total
counter_ind = 0
print('Individual standings:')
for k, v in sorted(total_points.items(), key=lambda x: (-x[1], x[0])):
    counter_ind += 1
    print(f'{counter_ind}. {k} -> {v}')
