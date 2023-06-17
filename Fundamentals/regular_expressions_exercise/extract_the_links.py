import re
pattern = r'www.([A-Za-z0-9-]+)\.([A-Za-z\-]+)+(\.[a-z0-9]+)*\b'
text = input()
while True:
    if text:
        matches = re.finditer(pattern, text)
        for match in matches:
            print(match.group(0))
    else:
        break
    text = input()