command = input()
dictionary = {}
submission_count = {}
dict_ban = {}
while command != 'exam finished':
    if '-banned' not in command:
        user_name, language, points_str = command.split('-')
        points = int(points_str)
        # submission
        if language not in submission_count:
            submission_count[language] = 0
        submission_count[language] += 1

        # user-points
        if user_name not in dictionary:
            dictionary[user_name] = points
        else:
            if points > dictionary[user_name]:
                dictionary[user_name] = points
    # ban
    else:
        user_name_ban, word = command.split('-')
        if user_name_ban in dictionary:
            del dictionary[user_name_ban]
    command = input()

dict_sorted = sorted(dictionary.items(), key=lambda kvpt: (-kvpt[1], kvpt[0]))
sub_sort = sorted(submission_count.items(), key=lambda kvpt: (-kvpt[1], kvpt[0]))
print('Results:')
for k, v in dict_sorted:
    print(f'{k} | {v}')
print('Submissions:')
for k, v in sub_sort:
    print(f'{k} - {v}')

