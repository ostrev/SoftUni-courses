first_type = {}
submissions = {}
best_candidate = {}
command = input()

while command != 'end of contests':
    contests, password = command.split(':')
    first_type[contests] = password

    command = input()

command = input()
while command != 'end of submissions':
    contests, password, username, points = command.split('=>')
    if contests in first_type and password == first_type[contests]:
        if username not in submissions:
            submissions[username] = {}
            submissions[username][contests] = int(points)
        else:
            if contests not in submissions[username]:
                submissions[username][contests] = int(points)
            else:
                if int(points) > submissions[username][contests]:
                    submissions[username][contests] = int(points)

    command = input()

for username_dic in submissions:
    sum_value = submissions[username_dic].values()
    total = sum(sum_value)
    best_candidate[username_dic] = total

max_value = max(best_candidate.values())
best_name = ""
for name, points in best_candidate.items():
    if max_value == points:
        best_name = name
print(f'Best candidate is {best_name} with total {max_value} points.')

sort_submission = dict(sorted(submissions.items(), key=lambda kvp: kvp[0]))
last_dict = {}
for k, value in sort_submission.items():
    last_dict[k] = {}
    sort_submission_two = sorted(value.items(), key=lambda kvp: kvp[1], reverse=True)
    last_dict[k] = dict(sort_submission_two)
print('Ranking:')
for k, v in last_dict.items():
    print(k)
    for con, poi in v.items():
        print(f'#  {con} -> {poi}')


print('Ranking:')
for k, v in sorted(submissions.items(), key=lambda x: x[0]):
    print(f'{k}')
    for kk,vv in sorted(v.items(), key=lambda x: -x[1]):
        print(f'#  {kk} -> {vv}')