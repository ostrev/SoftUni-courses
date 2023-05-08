chars = ["-", ",", ".", "!", "?"]
with open('text.txt', 'r') as file:
    for i, line in enumerate(file):
        if i % 2 == 0:
            reversed_str = reversed(line.strip().split())
            result = ' '.join(reversed_str)
            for char in chars:
                result = result.replace(char, '@')
            print(result)
        