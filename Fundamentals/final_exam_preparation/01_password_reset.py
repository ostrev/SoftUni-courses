password = input()

command = input()

while command != 'Done':
    data = command.split()
    if data[0] == 'TakeOdd':
        password = password[1::2]
        print(password)
    elif data[0] == 'Cut':
        index, len_str = data[1:]
        index = int(index)
        len_str = int(len_str)
        substring = password[index:index + len_str]
        password = password.replace(substring, '', 1)
        print(password)
    elif data[0] == 'Substitute':
        substring_1, substitute = data[1:]
        if substring_1 in password:
            password = password.replace(substring_1, substitute)
            print(password)
        else:
            print("Nothing to replace!")
    command = input()
print(f'Your password is: {password}')
