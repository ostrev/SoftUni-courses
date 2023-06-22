number = int(input())
search_word = input()
full_list = []

for _ in range(number):
    words = input()
    full_list.append(words)
print(full_list)
for index in range(1, len(full_list)+1):
    element = full_list[(index * -1)]
    if search_word not in element:
        full_list.remove(element)
print(full_list)
# can't use * -1 to iterate forom the end of the list.
# the same way like if I iterate from index[0]