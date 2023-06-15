first_str = input()
second_str = input()
command = input()
list_str = []
new_list = []
for i in command:
    list_str.append(ord(i))
for num in list_str:
    if ord(first_str) < num < ord(second_str):
        new_list.append(num)
print(sum(new_list))

