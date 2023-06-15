command = input().split()
res = ''
for word in command:
    res += word * len(word)

print(res)