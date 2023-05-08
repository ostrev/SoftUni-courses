import re

with open('text.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
    for index, line in enumerate(input_file):
        count = len(re.findall('[A-Za-z]', line))
        symbol_count = len(re.findall('[.,\\-\'":?!]', line))
        output_file.write(f"Line {index + 1}: {line.strip()} ({count})({symbol_count})\n")
