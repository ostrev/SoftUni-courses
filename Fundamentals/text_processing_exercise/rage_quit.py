command = input()
new_string = ''
result = ''
temp_str = ''
multi = 0

i = 0
while i < len(command):
    if not command[i].isdigit():
        temp_str += command[i].upper()
        i += 1
    else:
        # проверка дали цифрите са две
        if (i + 1) != len(command): # не е последен знак
            if command[i + 1].isdigit():
                multi = int(command[i] + command[i + 1])
                new_string = temp_str * multi
                result += new_string
                new_string = ''
                temp_str = ''
                i += 2
                continue
            else:
                new_string = temp_str * int(command[i])
                result += new_string
                new_string = ''
                temp_str = ''
                i += 1
            continue
        else: # последен знак е
            new_string = temp_str * int(command[i])
            result += new_string
            i += 1

unique = len(set(result))
print(f"Unique symbols used: {unique}")
print(result)

