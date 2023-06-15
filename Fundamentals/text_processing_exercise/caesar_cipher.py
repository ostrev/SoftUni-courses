data = input()
encrypt = ''
for char in data:
    encrypt += chr(ord(char) + 3)
print(encrypt)