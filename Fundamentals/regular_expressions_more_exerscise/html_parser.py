import re

line = input()
title = ''
content = ''
pattern_title = r'(?<=<title>)(.*)(?=<\/title>)'
matches = re.finditer(pattern_title, line)
for math in matches:
    title = math.group()

print(f'Title: {title}')

pattern_content = r'(?<=<body>)(.*)(?=<\/body>)'
matches = re.finditer(pattern_content, line)
for math in matches:
    content = math.group()

pattern_remove = r'<[a-z\/=".\s:]+>|\\n'
matches = re.finditer(pattern_remove, content)
for math in matches:
    remove = math.group()
    content = content.replace(remove, '')

print(f"Content: {content}")