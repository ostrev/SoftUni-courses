manipulated_list = input().split()
manipulated_list = list(map(int, manipulated_list))
command = input()
temp_max_min_even_odd = None
first_second_even_odd = []
only_odd = False
only_even = False
odd = False
even = False
for i in manipulated_list:
    if i % 2 == 0:
        even = True
    else:
        odd = True

if odd == True and even == False:
    only_odd = True
if even == True and odd == False:
    only_even = True

while command != 'end':
    command = command.split()
    first_second_even_odd = []
    if 'exchange' in command:
        if int(command[1]) >= len(manipulated_list) or int(command[1]) < 0:
            print('Invalid index')
        else:
            temp_man_list = manipulated_list[int(command[1]) + 1: len(manipulated_list)]
            temp_man_list += manipulated_list[0:int(command[1]) + 1]
            manipulated_list = temp_man_list
            # print(manipulated_list)
    elif 'max' in command:
        if 'odd' in command and only_even == False:
            temp_max_min_even_odd = max(i for i in manipulated_list if i % 2)
            for i in range(len(manipulated_list) - 1, -1, -1):
                if manipulated_list[i] == temp_max_min_even_odd:
                    temp_max_min_even_odd = i
                    print(temp_max_min_even_odd)
                    break
        elif 'even' in command and only_odd == False:
            temp_max_min_even_odd = max(i for i in manipulated_list if i % 2 == 0)
            for i in range(len(manipulated_list) - 1, -1, -1):
                if manipulated_list[i] == temp_max_min_even_odd:
                    temp_max_min_even_odd = i
                    print(temp_max_min_even_odd)
                    break
        else:
            print('No matches')

    elif 'min' in command:
        if 'odd' in command and only_even == False:
            temp_max_min_even_odd = min(i for i in manipulated_list if i % 2)
            for i in range(len(manipulated_list) - 1, -1, -1):
                if manipulated_list[i] == temp_max_min_even_odd:
                    temp_max_min_even_odd = i
                    print(temp_max_min_even_odd)
                    break
        elif 'even' in command and only_odd == False:
            temp_max_min_even_odd = min(i for i in manipulated_list if i % 2 == 0)
            for i in range(len(manipulated_list) - 1, -1, -1):
                if manipulated_list[i] == temp_max_min_even_odd:
                    temp_max_min_even_odd = i
                    print(temp_max_min_even_odd)
                    break
        else:
            print('No matches')

    elif 'first' in command:
        if int(command[1]) > len(manipulated_list) or int(command[1]) < 0:
            print('Invalid count')
            command = input()
            continue
        if command[2] == 'even':
            for i in manipulated_list:
                if i % 2 == 0:
                    first_second_even_odd.append(i)
            first_second_even_odd = first_second_even_odd[0:int(command[1])]
            if only_odd:
                print('[]')
            else:
                print(first_second_even_odd)
        else:
            for i in manipulated_list:
                if i % 2 != 0:
                    first_second_even_odd.append(i)
            first_second_even_odd = first_second_even_odd[0:int(command[1])]
            if only_even:
                print('[]')
            else:
                print(first_second_even_odd)

    elif 'last' in command:
        if int(command[1]) > len(manipulated_list) or int(command[1]) < 0:
            print('Invalid count')
            command = input()
            continue
        if command[2] == 'even':
            for i in manipulated_list:
                if i % 2 == 0:
                    first_second_even_odd.append(i)
            if len(first_second_even_odd) < int(command[1]):
                print(first_second_even_odd)
                command = input()
                continue
            else:
                first_second_even_odd = first_second_even_odd[len(first_second_even_odd) - int(command[1]):len(first_second_even_odd)]
            if only_odd:
                print('[]')
            else:
                print(first_second_even_odd)
        else:
            for i in manipulated_list:
                if i % 2 != 0:
                    first_second_even_odd.append(i)
            if len(first_second_even_odd) < int(command[1]):
                print(first_second_even_odd)
                command = input()
                continue
            else:
                first_second_even_odd = first_second_even_odd[len(first_second_even_odd) - int(command[1]):len(first_second_even_odd)]
            if only_even:
                print('[]')
            else:
                print(first_second_even_odd)
    command = input()
print(manipulated_list)
