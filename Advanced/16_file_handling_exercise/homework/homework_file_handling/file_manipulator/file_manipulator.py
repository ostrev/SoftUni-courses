from os import remove

command = input().split('-')
while not command[0] == 'End':
    action = command[0]
    name_of_file = command[1]
    if action == 'Create':
        with open(name_of_file, 'w') as file:
            pass
    elif action == 'Add':
        content_to_write = command[2]
        with open(name_of_file, 'a') as file:
            file.write(f'{content_to_write}\n')
    elif action == 'Delete':
        try:
            remove(name_of_file)
        except FileNotFoundError:
            print('An error occurred')
    elif action == 'Replace':
        try:
            old_text, new_text = command[2], command[3]
            with open(name_of_file, 'r+') as file:
                text = file.read().replace(old_text, new_text)
                file.seek(0)
                file.truncate()
                file.write(text)
        except FileNotFoundError:
            print('An error occurred')
    command = input().split('-')
