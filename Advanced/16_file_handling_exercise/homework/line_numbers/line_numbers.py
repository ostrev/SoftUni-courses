import re

punctiation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

with open('text.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
    for row, line  in enumerate(input_file):
        stripped_line = line.strip()
        letters_count = len(re.findall('[A-Za-z]', stripped_line))
        marks_count = len([c for c in stripped_line if  c in punctiation])
        output_file.write(f"Line {row + 1}: {stripped_line} ({letters_count}) ({marks_count}) \n")