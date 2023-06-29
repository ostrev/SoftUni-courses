first_sequence = input().split(', ')
second_sequence = input().split(', ')
result_list = []

for element in first_sequence:
    for i in range(len(second_sequence)):
        if element in second_sequence[i]:
            result_list.append(element)
            break
print(result_list)
