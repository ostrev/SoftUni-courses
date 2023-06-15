banned_list = input().split(', ')
text = input()

for i in range(0, len(banned_list)):
    text = text.replace(banned_list[i], "*" * len(banned_list[i]))
print(text)