import re

command = input()
pattern = r'%(?P<customer>[A-Z][a-z]+)%.*<(?P<product>\w+)>.*\|(?P<count>\d+)\|\D*(?P<price>[0-9]+\.?[0-9]+)\$'
total_income = 0
while command != 'end of shift':
    matches = re.finditer(pattern, command)
    for match in matches:
        customer = match.group('customer')
        product = match.group('product')
        quality = int(match.group(3))
        price = float(match.group(4))
        total_price = quality * price
        print(f"{customer}: {product} - {total_price:.2f}")
        total_income += total_price
    command = input()
print(f"Total income: {total_income:.2f}")