import re

pattern = r'(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))'
line = input()

matches = re.finditer(pattern, line)
for match in matches:
    print(match.group(), end=' ')
