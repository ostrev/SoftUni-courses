cut = input()
string = input()

while cut in string:
    string = string.replace(cut, '')

print(string)