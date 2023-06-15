usernames = input().split(', ')
output = ''
is_valid = True
for username in usernames:
    output = ''
    is_valid = True
    if 3 <= len(username) <= 16:
        for ch in username:
            if ch.isdigit():
                output += ch
            elif ch.isalpha():
                output += ch
            elif ch == '-':
                output += ch
            elif ch == '_':
                output += ch
            else:
                is_valid = False
                break
        if is_valid:
            print(output)