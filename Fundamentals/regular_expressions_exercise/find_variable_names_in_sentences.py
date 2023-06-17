import re
find = []
pattern = r'\b_([A-Za-z0-9]+)\b'
line = input()
matches = re.finditer(pattern, line)
for match in matches:
    find.append(match.group(1))

if find:
    print(','.join(find))
