text = input()

for index in range(0, len(text)):
    if text[index] == ':':
        print(f'{text[index]}{text[index + 1]}')
