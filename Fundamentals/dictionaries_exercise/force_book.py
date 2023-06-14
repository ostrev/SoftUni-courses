command = input()
my_dic = {}
loop_for = False
loop_if = False
while command != 'Lumpawaroo':
    data = command.split(' | ')
    if len(data) > 1:               # {force_side} | {force_user}
        side = data[0]
        user = data[1]
        for key, value in my_dic.items():
            if user in value:
                loop_if = True
                break

        if not loop_if:
              # вляза ли тук не изпълнявам долния иф
            if side not in my_dic:
                my_dic[side] = [user]
            else:
                my_dic[side].append(user)

    else:                           # {force_user} -> {force_side}
        data = command.split(' -> ')
        user = data[0]
        side = data[1]

        for key, value in my_dic.items():
            if user in value:
                my_dic[key].remove(user)
                loop_for = True
                for key, value in my_dic.items():
                    if user in value:
                        break
                if side not in my_dic:
                    my_dic[side] = [user]
                else:
                    my_dic[side].append(user)
                break

                    # вляза ли тук трябва да прескоча долния фор

        if not loop_for:
            for key, value in my_dic.items():
                if user in value:
                    break
            if side not in my_dic:
                my_dic[side] = [user]
            else:
                my_dic[side].append(user)

        print(f'{user} joins the {side} side!')
    command = input()

sorted_dic = sorted(my_dic.items(), key=lambda kvpt: (-len(kvpt[1]), kvpt[0]))
for side, user in sorted_dic:
    if user:
        print(f'Side: {side}, Members: {len(user)}')
        for i in sorted(user):
            print(f'! {i}')