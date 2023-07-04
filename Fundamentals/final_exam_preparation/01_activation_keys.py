activation_key = input()

command = input()

while command != 'Generate':
    data = command.split('>>>')
    if data[0] == 'Contains':
        substring = data[1]
        if substring in activation_key:
            print(f'{activation_key} contains {substring}')
        else:
            print("Substring not found!")
    elif data[0] == 'Flip':
        type_s, start_index, end_index = data[1:]
        start_index, end_index = int(start_index), int(end_index)
        if type_s == 'Upper':
            activation_key = activation_key[:start_index] + activation_key[
                                                            start_index:end_index].upper() + activation_key[end_index:]
        else:
            activation_key = activation_key[:start_index] + activation_key[
                                                            start_index:end_index].lower() + activation_key[end_index:]
        print(activation_key)
    elif data[0] == 'Slice':
        start_index, end_index = data[1:]
        activation_key = activation_key[:int(start_index)] + activation_key[int(end_index):]
        print(activation_key)

    command = input()
print(f"Your activation key is: {activation_key}")
