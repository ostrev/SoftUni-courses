key_list = [int(s) for s in input().split()]
list_decrypt = []
string_decrypt = ''
command = input()

while command != 'find':
    i_key = 0
    i = 0
    while i < len(command):
        string_decrypt += chr(ord(command[i]) - key_list[i_key])
        if i_key == len(key_list) - 1:
            i_key = 0
        else:
            i_key += 1
        i += 1

    command = input()
    list_decrypt.append(string_decrypt)
    string_decrypt = ''
for word in list_decrypt:
    start_point = word.find('&')
    end_point = word.find('&', start_point + 1)
    type = word[start_point + 1: end_point]
    start_point_c = word.find('<')
    end_point_c = word.find('>')
    coord = word[start_point_c + 1: end_point_c]
    print(f'Found {type} at {coord}')
