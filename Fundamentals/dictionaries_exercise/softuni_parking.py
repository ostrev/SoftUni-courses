numbers = int(input())
my_dic = {}

for _ in range(0, numbers):
    command = input().split()

    if command[0] == 'register':
        user_name, license_plate = command[1], command[2]
        if user_name not in my_dic:
            my_dic[user_name] = license_plate
            print(f'{user_name} registered {my_dic[user_name]} successfully')
        else:
            print(f'ERROR: already registered with plate number {my_dic[user_name]}')
    elif command[0] == 'unregister':
        user_name = command[1]
        if user_name not in my_dic:
            print(f'ERROR: user {user_name} not found')
        else:
            my_dic.pop(user_name)
            print(f'{user_name} unregistered successfully')

for k, v in my_dic.items():
    print(f'{k} => {v}')