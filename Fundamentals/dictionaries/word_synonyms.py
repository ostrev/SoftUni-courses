count = int(input())
my_dic = {}
while count > 0:
    key_word = input()
    synonym = input()
    if key_word not in my_dic:
        my_dic[key_word] = []
    my_dic[key_word].append(synonym)
    count -= 1
    key_word = ''
    synonym = ''
for word in my_dic:
    print(f'{word} - {", ".join(my_dic[word])}')