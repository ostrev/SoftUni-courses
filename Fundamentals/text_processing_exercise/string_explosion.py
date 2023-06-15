data = input()
new_string = ''
strength = 0
index = 0
while index < len(data):
    if data[index] == '>':
        new_string += data[index]
        index += 1
        strength += int(data[index])
        strength -= 1
    else:
        if strength > 0:
            strength -= 1
        else:
            new_string += data[index]
    index += 1
print(new_string)
