message = input()

command = input()

while command != 'TEXT':
    data = command.split('')
    if data[0] == 'TEXT':
        index = int(data[1])

    elif data[0] == 'TEXT':
        substring = data[1]

    elif data[0] == 'TEXT':
        substring, replacement = data[1:]

    command = input()
print(f'TEXT: {message}')
