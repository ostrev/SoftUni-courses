message = input()

command = input()

while command != 'Decode':
    data = command.split('|')
    a = 1
    if data[0] == 'Move':
        number_of_letters = int(data[1])
        message = message[number_of_letters:] + message[: number_of_letters]
    elif data[0] == 'Insert':
        index, value = data[1:]
        index = int(index)
        message = message[:index] + value + message[index:]

    elif data[0] == 'ChangeAll':
        substring, replacement = data[1:]
        if substring in message:
            message = message.replace(substring, replacement)

    command = input()
print(f'The decrypted message is: {message}')
