string_for_skip = input()
new_list = [s for s in string_for_skip]
number_list = [int(s) for s in new_list if s.isdigit()]
non_number_list = [s for s in new_list if not s.isdigit()]
take_list = [number_list[s] for s in range(len(number_list)) if s % 2 == 0]
skip_list = [number_list[s] for s in range(len(number_list)) if s % 2 != 0]
result_take_list = []
for i in range(0, len(take_list)):
    result_take_list += non_number_list[0:take_list[i]:1]
    non_number_list = non_number_list[take_list[i] + skip_list[i]::]
print(''.join(result_take_list))

