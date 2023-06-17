import re
line = sorted(s.strip() for s in input().split(","))
damage = 0
health = 0
mul_div = []

for message in line:
    pattern = r"[^0-9+\-*\/\.]"
    matches = re.finditer(pattern, message)
    for match in matches:
        health += ord(match.group())

    pattern = r"(\-?\d+(\.\d+)?)"
    matches = re.finditer(pattern, message)
    for match in matches:
        damage += float(match.group())

    pattern = r"[\*\/]"
    matches = re.finditer(pattern, message)
    for match in matches:
        mul_div.append(match.group())
    rev_mul = reversed(mul_div)

    for char in mul_div:
        if char == '*':
            damage = damage * 2
        else:
            damage = damage / 2

    print(f"{message} - {health} health, {damage:.2f} damage")
    damage = 0
    health = 0
    mul_div.clear()