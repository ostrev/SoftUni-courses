numbers = input().split()
# numbers = list(map(int, numbers))
text = str(input())
digits_sum = 0
new_string = ''
for numb in numbers:
    for digits in numb:
        digits_sum = digits_sum + int(digits)
    if len(text) < digits_sum:
        digits_sum = digits_sum - len(text)

    new_string += text[digits_sum]
    i = digits_sum
    text = text[:i] + text[i + 1:]
    digits_sum = 0
print(new_string)


