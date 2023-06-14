characters = input()
my_dic = {}
characters_str = ''
for char in characters:
    if char != ' ':
       characters_str += char

for char in characters_str:
    if char not in my_dic:
        my_dic[char] = 0
    my_dic[char] += 1
for key, value in my_dic.items():
    print(f'{key} -> {value}')
