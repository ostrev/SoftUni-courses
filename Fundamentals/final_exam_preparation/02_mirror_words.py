import re
pear_word = []
mirror_words = []
text = input()
pattern = r'(#|@)(?P<key>[A-Za-z]{3,})(\1)(\1)(?P<value>[A-Za-z]{3,})(\1)'

matches = re.finditer(pattern, text)

for match in matches:
    pear_word.append(match.groupdict())

if pear_word:
    print(f'{len(pear_word)} word pairs found!')
else:
    print('No word pairs found!')

for dict in pear_word:
    if dict['key'] == dict['value'][::-1]:
        string_mirror = f"{dict['key']} <=> {dict['value']}"
        mirror_words.append(string_mirror)
if mirror_words:
    print('The mirror words are:')
    print(f"{', '.join(mirror_words)}")
else:
    print("No mirror words!")
