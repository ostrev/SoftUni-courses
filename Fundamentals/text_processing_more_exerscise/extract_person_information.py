def get_name(command, name, age):
    name_start = command.find('@')
    name_end = command.find('|')
    age_start = command.find('#')
    age_end = command.find('*')
    name = command[name_start + 1:name_end]
    age = command[age_start + 1:age_end]
    return f'{name} is {age} years old.'

name = ''
age = ''
number = int(input())
for _ in range(number):
    command = input()
    print(get_name(command, name, age))

