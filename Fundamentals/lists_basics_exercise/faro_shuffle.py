single_string = input().split(' ')
count_shuffles = int(input())
mid_string = len(single_string) // 2

for count in range(count_shuffles):
    left_string = single_string[0:mid_string:]
    right_string = single_string[mid_string:len(single_string):]
    single_string = []
    for index in range(0, len(left_string)):
        single_string.append(left_string[index])
        single_string.append(right_string[index])
print(single_string)