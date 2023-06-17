import re

line = input()
word = input()
pattern = fr'{word}\b'

matches = re.findall(pattern, line, flags=re.I)
print(len(matches))