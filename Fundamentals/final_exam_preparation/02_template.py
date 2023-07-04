import re

text = input()
pattern = r'QQQQQ'

matches = re.finditer(pattern, text)


for match in matches:
    pass
