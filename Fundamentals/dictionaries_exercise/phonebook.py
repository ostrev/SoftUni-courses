command = input()
phonebook_dic = {}
while '-' in command:
    list_command = command.split('-')
    phonebook_dic[list_command[0]] = list_command[1]
    command = input()

for _ in range(int(command)):
    searched = input()
    if searched not in phonebook_dic:
        print(f'Contact {searched} does not exist.')
    else:
        print(f"{searched} -> {phonebook_dic[searched]}")

