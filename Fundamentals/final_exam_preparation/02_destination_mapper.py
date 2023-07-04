import re
locations = []
travel_points = 0
text = input()
pattern = r'(=|/)([A-Z][A-Za-z]{2,})(\1)'

matches = re.finditer(pattern, text)


for match in matches:
    locations.append(match.group(2))
    travel_points += int(len(match.group(2)))

print(f"Destinations: {', '.join(locations)}")
print(f'Travel Points: {travel_points}')