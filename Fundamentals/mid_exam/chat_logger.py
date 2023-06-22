message_list = []
command = input()

while command != 'end':
    message = command.split()
    if message[0] == 'Chat':
        value_string = message[1]
        message_list.append(value_string)

    elif message[0] == 'Delete':
        value_string = message[1]
        if value_string in message_list:
            message_list.remove(value_string)

    elif message[0] == 'Edit':
        value_string = message[1]
        edit_string = message[2]
        if value_string in message_list:
            index_e = message_list.index(value_string)
            message_list[index_e] = edit_string

    elif message[0] == 'Pin':
        value_string = message[1]
        if value_string in message_list:
            message_list.remove(value_string)
            message_list.append(value_string)

    elif message[0] == 'Spam':
        for i in message[1::]:
            message_list.append(i)

    command = input()

print('\n'.join(message_list))

