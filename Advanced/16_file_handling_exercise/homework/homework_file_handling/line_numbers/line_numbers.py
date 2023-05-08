import re

with open('text.txt') as file:
    text = file.readlines()
    for index in range(len(text)):
        with open('output.txt', 'a') as file_two:
            pattern_for_symbols = r'[-,\'\-!?:;.]'
            pattern_for_letters = r'[A-Za-z]'
            symbols_count = len(re.findall(pattern_for_symbols, text[index]))
            letters_count = len(re.findall(pattern_for_letters, text[index]))
            file_two.write(f'Line {index + 1}: {text[index].strip()} ({letters_count}) ({symbols_count})\n')
