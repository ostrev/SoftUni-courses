command = input()
count = 1
my_dic = {}
key = ''
value = 0
while command != 'stop':
    if count % 2 == 0:
        value = int(command)
    else:
        key = command

    if key not in my_dic:
        my_dic[key] = 0
    elif key in my_dic and my_dic[key] == 0:
        my_dic[key] += value
    elif key in my_dic and count % 2 == 0:
        my_dic[key] += value
    command = input()
    count += 1
for key, value in my_dic.items():
    print(f'{key} -> {value}')
