import re


with open('text.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
    for row, line in enumerate(input_file):
        stripped_line = line.strip()
        letters_count = len(re.findall('[A-Za-z]', stripped_line))
        marks_count = len(re.findall('[,.\\-\'":?!]', stripped_line))
        output_file.write(f'Line {row + 1}: {stripped_line} ({letters_count})({marks_count})\n')

import re

with open('text.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
    for index, line in enumerate(input_file):
        count = len(re.findall('[A-Za-z]', line))
        symbol_count = len(re.findall('[.,\\-\'":?!]', line))
        output_file.write(f"Line {index + 1}: {line.strip()} ({count})({symbol_count})\n")
