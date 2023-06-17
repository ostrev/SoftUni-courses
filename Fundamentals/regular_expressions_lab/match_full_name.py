import re
line = input()
pattern = r'\b[A-Z][a-z]+\s[A-Z][a-z]+\b'

matches = re.findall(pattern, line)

print(*matches)