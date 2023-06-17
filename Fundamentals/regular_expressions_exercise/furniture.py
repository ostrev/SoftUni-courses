import re
patter = r'^>>([A-Za-z0-9]+)<<(\d+\.?\d+)!(\d+)\b'
furniture = []
total_sum = 0
line = input()
while line != 'Purchase':
    matches = re.finditer(patter, line)
    for match in matches:
        name, price, quantity = match.groups()
        furniture.append(name)
        total_sum += float(price) * int(quantity)
    line = input()

print('Bought furniture:')
for item in furniture:
    print(item)
print(f'Total money spend: {total_sum:.2f}')