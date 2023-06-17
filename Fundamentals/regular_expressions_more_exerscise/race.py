import re

participants = input().split(", ")
command = input()
name = ''
distance = []
race_dictionary = {}

for participant in participants:
    race_dictionary[participant] = 0

while command != 'end of race':
    pattern_of_letters = r"[a-zA-Z]"
    pattern_of_digits = r"\d"
    matches_l = re.finditer(pattern_of_letters, command)
    matches_d = re.findall(pattern_of_digits, command)

    for match in matches_l:
        name += match.group()

    distance = [int(s) for s in matches_d]

    if name in race_dictionary:
        race_dictionary[name] += sum(distance)

    name = ''
    distance.clear()
    command = input()
result = sorted(race_dictionary.items(), key=lambda kvp: kvp[1], reverse=True)


print(f'1st place: {result[0][0]}')
print(f'2nd place: {result[1][0]}')
print(f'3rd place: {result[2][0]}')
