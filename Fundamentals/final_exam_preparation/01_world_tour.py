message = input()

command = input()

while command != 'Travel':
    data = command.split(':')
    if data[0] == 'Add Stop':
        index = int(data[1])
        string_tour = data[2]
        if 0 <= index < len(message):
            message = message[:index] + string_tour + message[index:]
        print(message)
    elif data[0] == 'Remove Stop':
        start_index = int(data[1])
        end_index = int(data[2])
        if 0 <= start_index < len(message) and 0 <= end_index < len(message):
            message = message[:start_index] + message[end_index+1:]
        print(message)
    elif data[0] == 'Switch':
        old, new = data[1:]
        if old in message:
            message = message.replace(old, new)
        print(message)
    command = input()

print(f'Ready for world tour! Planned stops: {message}')
