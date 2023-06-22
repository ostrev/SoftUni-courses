string_for_invert = input()
list_string = string_for_invert.split()
invert_list = []
for index in range(len(list_string)):
    element = list_string[index]
    element = int(element)
    element = element * -1
    invert_list.append(element)
print(invert_list)
