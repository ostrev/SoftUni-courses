import re

number = int(input())

for _ in range(number):
    is_valid = False
    text = input()
    pattern = r'\|(?P<boss>[A-Z]{3,})\|:#(?P<title>[A-Za-z]+\s[a-zA-Z]+)#'
    matches = re.finditer(pattern, text)

    for match in matches:
        print(f"{match.groupdict()['boss']}, The {match.groupdict()['title']}")
        print(f">> Strength: {len(match.groupdict()['boss'])}")
        print(f">> Armour: {len(match.groupdict()['title'])}")
        is_valid = True
    if not is_valid:
        print("Access denied!")

