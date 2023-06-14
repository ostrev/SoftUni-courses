list_of_characters = input().split(", ")
my_dic = {}
for i in list_of_characters:
    my_dic[i] = ord(i)
print(my_dic)

list_of_characters = input().split(", ")
print({key:ord(key) for key in list_of_characters})