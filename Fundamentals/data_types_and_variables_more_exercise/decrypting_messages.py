key = int(input())
number_lines = int(input())
decrypt = ''
for i in range(1, number_lines+1):
    char = input()
    decrypt += chr((ord(char)) + key)
print(decrypt)