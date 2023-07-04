import re

number = int(input())
count = 0
while count < number:
    text = input()
    pattern = r'@#{1,}([A-Z][A-Za-z0-9]{4,}[A-Z])@#{1,}'

    matches = re.finditer(pattern, text)
    pat_group = r'\d'
    product_group_list = re.findall(pat_group, text)
    product_group = ''
    barcode = []
    for num in product_group_list:
        product_group += num
    for match in matches:
        barcode.append(match.group())
    if barcode:
        if product_group:
            print(f'Product group: {product_group}')
        else:
            print('Product group: 00')
    else:
        print('Invalid barcode')
    count += 1
