import re
ord_list = []
number = int(input())

for _ in range(number):
    text = input()
    pattern = r'\!(?P<command>[A-Z][a-z]{2,})\!:\[(?P<message>[A-Za-z]{8,})\]'
    matches = re.search(pattern, text)
    if matches:
        text = matches.group(2)
        for char in text:
            ord_list.append(str(ord(char)))
        print(f'{matches.group(1)}: {" ".join(ord_list)}')
    else:
        print('The message is invalid')

