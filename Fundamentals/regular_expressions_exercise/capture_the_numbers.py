import re
pattern = r'\d+'
line = input()
while line:
    matches = re.findall(pattern, line)
    for match in matches:
        print(match, end=" ")
    line = input()
