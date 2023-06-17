import re
pattern = r'\b(?P<day>\d{2})(\.|-|/)(?P<month>[A-Z][a-z]{2})(\2)(?P<year>\d{4})\b'

dates = input()

matches = re.finditer(pattern, dates)

for match in matches:
    group_dict = match.groupdict()
    print(f"Day: {group_dict['day']}, Month: {group_dict['month']}, Year: {group_dict['year']}")
