import re
list_number = []
pattern = r'\+359(\s|-)2(\1)\d{3}(\1)\d{4}\b'
command = input()
matches = re.finditer(pattern, command)
for match in matches:
    match_str = match.group(0)
    list_number.append(match_str)

print(', '.join(list_number))

