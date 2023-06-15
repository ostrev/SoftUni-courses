def alfabet(letter):
    letter = letter.lower()
    for i in range(1, 27):
        alfa_key[chr(96 + i)] = i
    return alfa_key[letter]

alfa_key = {}
temp_result = 0
result = 0
digit = 0
before = ''
after = ''

data = input().split()
for i in range(0, len(data)):
    for dig in data[i]:
        index = data[i].find(dig)
        if dig.isdigit():
            digit += dig
        elif dig.isalpha() and index == 0:
            before = dig
        else:
            after = dig

# for i in data:
#     before = i[0]
#     after = i[len(i) - 1:]
#     digit = int(i[1:len(i) - 1])

    if before.isupper():
        temp_result = int(digit) / alfabet(before)
    elif before.islower():
        temp_result = int(digit) * alfabet(before)

    if after.isupper():
        temp_result -= alfabet(after)
    elif after.islower():
        temp_result += alfabet(after)

    result += temp_result
    digit = ''

print(f'{result:.2f}')

