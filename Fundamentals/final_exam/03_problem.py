# dictionary

text = input()
dictionary = {}
list_words = text.split(' | ')
for kvp in list_words:
    kv = kvp.split(': ')
    word = kv[0]
    value = kv[1]
    if word not in dictionary:
        dictionary[word] = []
    dictionary[word].append(value)
test_words = input().split(" | ")
command = input()

test_dic = {}
new_test = {}
if command == 'Test':
    for word in test_words:
        if word in dictionary: # test for same words
            test_dic[word] = dictionary[word]

    for key, v in test_dic.items():
        list_for_sort = v
        sort_list = sorted(list_for_sort, key=len, reverse=True)
        new_test[key] = sort_list

    for word,value in new_test.items():
        print(f'{word}:')
        for val in value:
            print(f' -{val}')

elif command == 'Hand Over':
    sort_dictionary = sorted(dictionary, key=lambda kvpt: kvpt[0])
    for key in sort_dictionary:
        print(f'{key}', end= " ")
