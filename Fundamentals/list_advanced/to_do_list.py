to_do_list = [0] * 10
command = input()
to_do = []
while not command == 'End':
    command = command.split('-')
    importance = int(command[0])
    note = command[1]
    to_do_list.insert(importance-1, note)
    to_do_list.pop(importance)
    command = input()

print([el for el in to_do_list if not el == 0])
# for el in to_do_list:
#     if not el == 0:
#         to_do.append(el)
# print(to_do)