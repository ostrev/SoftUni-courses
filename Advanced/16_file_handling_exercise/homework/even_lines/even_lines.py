replacer = ['-', ',', '.', '!', '?']

with open('text.txt', 'r') as file:
    for row, line in enumerate(file):
        if row % 2 == 0:
            result = ' '.join(line.strip().split()[::-1])
            for char in replacer:
                result = result.replace(char, '@')
            print(result)