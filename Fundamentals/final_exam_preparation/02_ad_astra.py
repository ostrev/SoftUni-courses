import re

text = input()
pattern = r'(#|\|)([A-Za-z\s]+)(\1)(\d{2}/\d{2}/\d{2})(\1)(\d+)(\1)'

matches = re.finditer(pattern, text)
items = []
date = []
calories = []
days = 0
for match in matches:
    items.append(match.group(2))
    date.append(match.group(4))
    calories.append(int(match.group(6)))
days = int(sum(calories)/2000)
print(f'You have food to last you for: {days} days!')

for i in range(len(items)):
    print(f'Item: {items[i]}, Best before: {date[i]}, Nutrition: {calories[i]}')
