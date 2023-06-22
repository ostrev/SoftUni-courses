number = int(input())
search_word = input()
full_list = []

for _ in range(number):
    words = input()
    full_list.append(words)
print(full_list)
for index in range(len(full_list)-1, -1, -1):
    element = full_list[index]
    if search_word not in element:
        full_list.remove(element)
print(full_list)