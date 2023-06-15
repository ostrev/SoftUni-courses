data = input()
result = ''
for index in range(0, len(data)):
    if index != len(data) - 1:
        if data[index] != data[index + 1]:
            result += data[index]
    else:
        result += data[index]
print(result)