input_string = input().split(', ')
count = 0
input_string = list(map(int, input_string))

while 0 in input_string:
    input_string.remove(0)
    count += 1
for value in range(count):
    input_string.append(0)
print(input_string)