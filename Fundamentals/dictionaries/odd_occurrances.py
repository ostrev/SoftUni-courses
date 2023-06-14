words = input().split(" ")
my_dic = {}

for word in words:
    word = word.lower()
    if word not in my_dic:
        my_dic[word] = 0
    my_dic[word] += 1
for key, value in my_dic.items():
    if value % 2 != 0:
        print(key, end=' ')