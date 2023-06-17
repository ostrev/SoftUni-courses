import re
pattern = r'(?<=\s)([a-z0-9]+[-\.\_a-z0-9]*)@([a-z]+)(-[a-z]+)*\.([a-z\.]+)\b'

command = input()
matches = re.finditer(pattern, command)
for match in matches:
    print(match.group(0))