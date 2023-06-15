command = input().split()
total = 0
dif = abs(len(command[0]) - len(command[1]))
first = command[0]
second = command[1]
for ch1, ch2 in zip(command[0], command[1]):
    total += (ord(ch1) * ord(ch2))
if len(command[0]) < len(command[1]):
    for index in range(int(len(second)) - 1, (int(len(second)) - dif) - 1, -1):
        total += ord(second[index])
elif len(first) > len(second):
    for index in range(int(len(first)) - 1, (int(len(first)) - dif) - 1, -1):
        total += ord(first[index])
print(total)