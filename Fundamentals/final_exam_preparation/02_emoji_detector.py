import re
emojis = []
cool_emojis = []
threshold = 1
text = input()
patt_thresh = r'\d'
matches_num = [int(s) for s in re.findall(patt_thresh, text)]
for num in matches_num:
    threshold *= num
print(f'Cool threshold: {threshold}')

pattern = r'(::|\*\*)([A-Z][a-z]{2,})(\1)'

matches = re.finditer(pattern, text)
total_points = 0
for match in matches:
    emojis.append(match.group(2))
    cool_emojis.append(match.group())

print(f'{len(emojis)} emojis found in the text. The cool ones are:')
for emoji in range(len(emojis)):
    for i in emojis[emoji]:
        total_points += ord(i)

    if total_points > threshold:
        print(cool_emojis[emoji])
    total_points = 0

