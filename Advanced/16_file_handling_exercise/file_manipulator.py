from os import path, remove
while True:
    line = input()
    if line == 'End':
        break
    line_split = line.split('-')
    command = line_split[0]
    name = line_split[1]

    if command == 'Create':
        open(name, 'w').close()
    elif command == 'Add':
        content = line_split[2]
        with open(name, 'a') as file:
            file.write(content + '\n')
    elif command == 'Delete':
        if path.exists(name):
            remove(name)
        else:
            print('An error occurred')
    elif command == 'Replace':
        old = line_split[2]
        new = line_split[3]
        if not path.exists(name):
            print('An error occurred')
            continue

        with open(name, 'r+') as file:
            new_file = file.read().replace(old, new)
            file.seek(0)
            file.truncate()
            file.write(new_file)



