# first_string = input()
# second_string = input()
#
# new_string = ''
# for i, j in zip(first_string, second_string):
#     if i != j:
#         new_string += j
#     else:
#         new_string += i
# print(new_string)

starting_word = input()
aim_mutated_word = input()

result = ""
previous_str = starting_word

for index in range(len(starting_word)):
    for i in range(index + 1):
        result += aim_mutated_word[i]
    for i in range(index + 1, len(aim_mutated_word)):
        result += starting_word[i]
    if not result == previous_str:
        print(result)
    previous_str = result
    result = ""