message = input().split()
word_list = []
first_element = ''
word_no_dig = ''
temp_second_digit = ''
temp_last_digit = ''
word_for_list = ''
word_temp = ''
for word in message:
    for digits in word:
        if digits.isdigit():
            first_element += digits
        else:
            word_no_dig += digits
    first_element = chr(int(first_element))
    for i in range(0, len(word_no_dig)):
        if i == 0:
            temp_second_digit = word_no_dig[i]
        elif i == len(word_no_dig) - 1:
            temp_last_digit = word_no_dig[i]
        else:
            word_temp += word_no_dig[i]
    word_for_list = first_element + temp_last_digit + word_temp + temp_second_digit
    word_list.append(word_for_list)
    first_element = ''
    word_no_dig = ''
    temp_second_digit = ''
    temp_last_digit = ''
    word_for_list = ''
    word_temp = ''
print(' '.join(word_list))
