import re
number = int(input())

for _ in range(number):
    text = input()
    pattern = r'(\*|@)([A-Z][a-z]{2,})(\1):\s\[([a-zA-z])\]\|\[([a-zA-z])\]\|\[([a-zA-z])\]\|$'

    matches = re.search(pattern, text)
    if matches:
        print(f"{matches.group(2)}: {ord(matches.group(4))} {ord(matches.group(5))} {ord(matches.group(6))}")
    else:
        print('Valid message not found!')